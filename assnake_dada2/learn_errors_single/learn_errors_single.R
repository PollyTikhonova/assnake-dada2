args <- commandArgs(TRUE)
read_table_loc <- c(args[[1]])
out_loc <- c(args[[2]])
randomize <- as.logical(args[[3]])
MAX_CONSIST <- as.integer(args[[4]])
threads <- as.integer(args[[5]])

library("dada2")
reads <- read.table(file = read_table_loc, sep = '\t', header = TRUE)

err <- learnErrors(as.character(reads$R1), multithread=threads, randomize=randomize, MAX_CONSIST=MAX_CONSIST)

saveRDS(err, out_loc)

