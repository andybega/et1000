
library(jsonlite)
words <- read.csv("counts.csv")
words$Rank <- 1:nrow(words)
words <- words[, c("Rank", "Word", "Count")]
write_json(words, "words.json", dataframe = "values", pretty = FALSE)