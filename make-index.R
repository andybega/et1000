
library(jsonlite)

# Read and format the word data so that we get a 
# wordData = [...] JSON-formatted string
words <- read.csv("counts.csv")
words <- words[, c("Rank", "Word")]
words <- toJSON(words, dataframe = "values", pretty = FALSE)
# pre-pend the object definition
words <- paste0("wordData = ", words)

# Inset the word data into the html template
index <- readLines("template/index.html")
line <- grep("wordData = ", index)
index[line] <- words
writeLines(index, "docs/index.html")
