
library(jsonlite)
words <- read.csv("counts.csv")
words$Rank <- 1:nrow(words)
words <- words[1:100, c("Rank", "Word", "Count")]
write_json(words, "words.json", dataframe = "values", pretty = TRUE)