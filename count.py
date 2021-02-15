from estnltk.corpus_processing.parse_enc import parse_enc_file_iterator
from estnltk.corpus_processing.parse_ettenten import parse_ettenten_corpus_file_iterator
from estnltk import Text
from collections import Counter
import pandas as pd
from tqdm import tqdm
import pickle

input_file = "etnc19_web_2019.prevert"
docs = parse_ettenten_corpus_file_iterator(input_file)

# Basic progress counter
docs = tqdm(docs)

# Build up list of lemma counts in each doc item
n = 1
max_docs = 5000
wf = Counter()
for text_obj in docs:
	text_obj = text_obj.tag_layer('morph_analysis')
	lc  = text_obj.morph_analysis.groupby(['lemma']).count
	res = Counter({k[0]:v for k, v in lc.items()})
	wf += res
	n = n + 1
	if (n > max_docs):
		break

# Remove not-really-lemmas
ignore = ['s', '.', ',', '"', '-', '?', '(', ')', ':', 'OK', '!', 'NB', '§',
          ';', '...', '/', '_', 'OÜ', '*', '`', '’', '$', '[', ']',
          ':)', 'AS', 'I', 'II', '..', 'nr', '=', '+', '€', 'a', '•',
          '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', 'ca', '&',
          '2018.', '2019.']
for word in list(wf):
    if word in ignore:
        del wf[word]
    if word.isdigit():
        del wf[word]

# Save the lemma freq Counter, since it takes a long time to run it
with open('wf.pickle', 'wb') as outputfile:
    pickle.dump(wf, outputfile)

wf.most_common(50)

# Convert to data frame and write top 1000 to CSV
counts = pd.DataFrame.from_dict(wf, orient='index').reset_index()
counts = counts.rename(columns={'index':'Word', 0:'Count'})
counts = counts.sort_values(by=['Count'], ascending=False)
counts["Frequency"] = counts["Count"] / counts["Count"].sum()

counts = counts.head(1000)
counts.to_csv("counts.csv", index = False)

