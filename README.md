1,000 most common Estonian words
================================

(Work in progress)

What are the 1,000 most common Estonian words? I'm an English speak learning Estonian, and had trouble finding the answer.

This was made using the Estonian Web 2019 corpus from the 2019 Estonian reference corpus

\+ 

Estonian is a "morphologically rich", as I learned the experts call it, language. Words change a lot depending on the grammatical context. For example "pood", "poodi", "poes", and "poest" are all forms of the same word (lemma), "pood", which means "store" (the forms above are a store, to the store, in the store, from the store). I'd like all of those forms to count for the same canonical form of the word, rather than counting them up separately. I used the Estonian natural language toolkit ([EstNLTK](https://github.com/estnltk/estnltk)) lemmatizer for this.  

\+

Some very hacky scripts to get a basic website with the words. 

The data file for the full 2019 reference corpus can be downloaded from https://metashare.ut.ee/repository/browse/estonian-national-corpus-2019/cd9633fab22e11eaa6e4fa163e9d4547b71a2df64d1f43f1ac26dbd8508ea951/. Although I downloaded the whole thing, I only used the Estonian 2019 web corpus (`etnc19_web_2019.prevert`). The file is too big for git. 

Following the [`estnltk`](https://github.com/estnltk/estnltk) install instructions, I created a separate Python 3.7 environment for it. To run the scripts above:

```bash 
conda activate py37
python3 counts.py
# this will write counts.csv
Rscript counts2json.R
# pull top 100 from CSV to words.json
```

From there I manually pulled the JSON blob and pasted it into `index.html`. (I don't know Javascript...)

For a basic website, show common words as html table?

Ideas:

- Clean, minimal table with order, lemma, freq
- Add bar graph for freq?
- Add search option to filter table
- Add POS tag 
- Add POS tag to search option, i.e. i can search most common nouns, verbs, etc. 

Searchable HTML table: https://www.w3schools.com/howto/howto_js_filter_table.asp
JS scripts for search: https://stackoverflow.com/questions/9127498/how-to-perform-a-real-time-search-and-filter-on-a-html-table