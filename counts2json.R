
library(jsonlite)
words <- read.csv("counts.csv")
words <- words[, c("Rank", "Word")]
write_json(words, "words.json", dataframe = "values", pretty = FALSE)