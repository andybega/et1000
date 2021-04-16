from estnltk.corpus_processing.parse_enc import parse_enc_file_iterator
from estnltk.corpus_processing.parse_ettenten import parse_ettenten_corpus_file_iterator
from estnltk import Text
from collections import Counter
import pandas as pd
from tqdm import tqdm
import pickle
import yaml
import logging
log = logging.getLogger("et1000")

input_file = "etnc19_web_2019.prevert"
docs = parse_ettenten_corpus_file_iterator(input_file)

# Basic progress counter
docs = tqdm(docs)

# Build up list of lemma counts in each doc item
n = 1
max_docs = 10000
wf = Counter()
for text_obj in docs:
	text_obj = text_obj.tag_layer('morph_analysis')
	lc  = text_obj.morph_analysis.groupby(['lemma', 'partofspeech']).count
	res = Counter({k:v for k, v in lc.items()})
	wf += res
	n = n + 1
	if (n > max_docs):
		break

# Removing non-lemmas is easier by re-loading the word dict than running that 
# loop above again
pickle.dump(wf, open('wf.pickle', 'wb'))
wf = pickle.load(open('wf.pickle', 'rb'))

# Remove by part of speech
# https://github.com/estnltk/estnltk/blob/version_1.6/tutorials/nlp_pipeline/A_02_morphology_tables.ipynb
# H: proper noun
# Y: abbreviation
# Z: punctuation
ignore = ['H', 'Y', 'Z']
for word in list(wf):
    if word[1] in ignore:
        del wf[word]

# Remove any other words starting with a capital letter, e.g. "CX-3"
for word in list(wf):
    if word[0].isupper():
        #log.info('Removing \'' + word + '\'')
        del wf[word]

# Remove any leftover idiosyncratic words as well as words starting with a 
# digit, e.g. dates. 
ignore = ['s', '.', ',', '"', '-', '?', '(', ')', ':', 'OK', '!', 'NB', '§',
          ';', '...', '/', '_', 'OÜ', '*', '`', '’', '$', '[', ']',
          ':)', 'AS', 'I', 'II', '..', 'nr', '=', '+', '€', 'a', '•',
          '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', 'ca', '&',
          '2017.', '2018.', '2019.', '20.']

for word in list(wf):
    if word[0] in ignore:
        del wf[word]
    if word[0].isdigit():
        del wf[word]

wf.most_common(10)

# Convert to data frame and write top 1000 to CSV
counts = pd.Series(wf).to_frame(name='Count')
counts.index = counts.index.set_names(['Word', 'POS'])
counts.reset_index(inplace=True)

# sort and re-index
counts = counts.sort_values(by=['Count'], ascending=False)
counts = counts.reset_index(drop=True)

# add Rank columns
counts['Rank'] = counts.index + 1

# Record the total number of words in case we want frequency later
stats = {"max_docs": max_docs,
         "lemmas": counts.shape[0],
         "total_words": counts['Count'].sum().item()}
with open(r'count-stats.yml', 'w') as file:
    documents = yaml.dump(stats, file, sort_keys=False)

# Save the top 1,000 only
counts = counts[['Rank', 'Word', 'POS', 'Count']]
counts = counts.head(1000)
counts.to_csv("counts.csv", index = False)


