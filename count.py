from estnltk.corpus_processing.parse_enc import parse_enc_file_iterator
from estnltk.corpus_processing.parse_ettenten import parse_ettenten_corpus_file_iterator
from estnltk import Text
from collections import Counter
import pandas as pd
from tqdm import tqdm
import pickle
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
	lc  = text_obj.morph_analysis.groupby(['lemma']).count
	res = Counter({k[0]:v for k, v in lc.items()})
	wf += res
	n = n + 1
	if (n > max_docs):
		break

# Removing non-lemmas is easier by re-loading the word dict than runnng that 
# loop above again
#wf = pickle.load(open('wf.pickle', 'rb'))

# Remove not-really-lemmas
ignore = ['s', '.', ',', '"', '-', '?', '(', ')', ':', 'OK', '!', 'NB', '§',
          ';', '...', '/', '_', 'OÜ', '*', '`', '’', '$', '[', ']',
          ':)', 'AS', 'I', 'II', '..', 'nr', '=', '+', '€', 'a', '•',
          '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', 'ca', '&',
          '2017.', '2018.', '2019.']

for word in list(wf):
    if word in ignore:
        del wf[word]
    if word[0].isdigit():
        del wf[word]

# Remove proper nouns (starting with capital letter)
for word in list(wf):
    if word[0].isupper():
        #log.info('Removing \'' + word + '\'')
        del wf[word]

# Save the lemma freq Counter, since it takes a long time to run it
with open('wf.pickle', 'wb') as outputfile:
    pickle.dump(wf, outputfile)

wf.most_common(10)

# Convert to data frame and write top 1000 to CSV
counts = pd.DataFrame.from_dict(wf, orient='index').reset_index()
counts = counts.rename(columns={'index':'Word', 0:'Count'})
counts = counts.sort_values(by=['Count'], ascending=False)
counts = counts.reset_index(drop = True)
counts["Frequency"] = counts["Count"] / counts["Count"].sum()
counts['Rank'] = counts.reset_index().index + 1
counts = counts[['Rank', 'Word', 'Count', 'Frequency']]

counts = counts.head(1000)
counts.to_csv("counts.csv", index = False)

