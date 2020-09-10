args <- commandArgs(TRUE)

# LOAD PARAMS
dada <- readRDS(args[[1]])
out <- c(args[[2]])

library("dada2")
seqtab <- makeSequenceTable(dada)
saveRDS(seqtab, out)

