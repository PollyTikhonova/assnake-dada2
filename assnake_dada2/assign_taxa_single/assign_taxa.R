args <- commandArgs(TRUE)

# LOAD PARAMS
seqtab <- readRDS(args[[1]])
out <- c(args[[2]])
db_loc <- c(args[[3]])
db2_loc <- c(args[[4]])
threads <- as.integer(args[[5]])

library("dada2")
taxa <- assignTaxonomy(seqtab, db_loc, multithread=threads)
taxa <- addSpecies(taxa, db2_loc)
saveRDS(taxa, out)

