
suppressPackageStartupMessages({
  library(jsonlite)
  library(dplyr)
})


# Read and format the word data so that we get a
# wordData = [...] JSON-formatted string
words <- read.csv("counts.csv")

dict <- data.frame(
  POS = c("S", "V", "D", "A", "C", "U", "K", "P", "J", "N", "G", "I", "O"),
  type = c("noun", "verb", "adverb", "adjective", "adjective", "adjective", "adposition", "pronoun", "conjunction", rep("other", 4))
)

words %>%
  left_join(dict) %>%
  count(type) %>%
  arrange(desc(n))

words <- words[, c("Rank", "Word", "POS")]
words <- toJSON(words, dataframe = "values", pretty = FALSE)

# pre-pend the JS object definition
words <- paste0("wordData = ", words)

# Insert the word data into the html src
index <- readLines("src/index.html")
line <- grep("wordData = ", index)
index[line] <- words
writeLines(index, "docs/index.html")

other_files <- setdiff(dir("src/"), "index.html")
invisible(file.copy(file.path("src", other_files), "docs/", overwrite = TRUE))
