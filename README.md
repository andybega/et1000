1,000 most common Estonian words
================================

What are the 1,000 most common Estonian words? I'm an English speaker learning Estonian, and had trouble finding the answer. 

This was made using the Estonian Web 2019 corpus from the 2019 Estonian reference corpus.

Estonian is a "morphologically rich" language, as I learned the experts call it. Words change a lot depending on the grammatical context. For example "pood", "poodi", "poes", and "poest" are all forms of the same underlying canonical word (lemma), "pood". Which by the way means "store"; the forms above are _a store_, _to the store_, _in the store_, _from the store_. I'd like all of those forms to count for the same canonical form of the word, rather than counting them up separately. I used the lemmatizer in the Estonian natural language toolkit ([EstNLTK](https://github.com/estnltk/estnltk)) for this.  

Some very hacky scripts to get a basic website with the words. 

The data file for the full 2019 reference corpus can be downloaded from https://metashare.ut.ee/repository/browse/estonian-national-corpus-2019/cd9633fab22e11eaa6e4fa163e9d4547b71a2df64d1f43f1ac26dbd8508ea951/. Although I downloaded the whole thing, I only used the Estonian 2019 web corpus (`etnc19_web_2019.prevert`). The file is too big for git. 

Following the [`estnltk`](https://github.com/estnltk/estnltk) install instructions, I created a separate Python 3.7 environment for it. To run the scripts above:

```bash 
conda activate py37
python3 count.py
# this will write counts.csv and wf.pickle
Rscript make-index.R
# this will insert the word data into index.html
```

Finally, _Are these really the 1,000 most common words in Estonian?_ I don't know, I'm not a linguist. I am sure that these are the 1,000 most common lemmas in the first 10,000 documents in the Estonian 2019 web corpus. How representative that is of the language in other contexts, I don't know. 
