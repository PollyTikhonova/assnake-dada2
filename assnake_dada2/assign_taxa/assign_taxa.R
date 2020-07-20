args <- commandArgs(TRUE)

# LOAD PARAMS
seqtab <- readRDS(args[[1]])
out <- c(args[[2]])
db_loc <- c(args[[3]])
threads <- as.integer(args[[4]])

library("dada2")
taxa <- assignTaxonomy(seqtab, db_loc, multithread=threads)
saveRDS(taxa, out)

