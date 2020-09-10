args <- commandArgs(TRUE)

# LOAD PARAMS
read_table_loc <- c(args[[1]])
err <- readRDS(args[[2]])
out <- c(args[[3]])
derep_out  <- c(args[[4]])

library("dada2")
reads <- read.table(file = read_table_loc, sep = '\t', header = TRUE)
derep <- derepFastq(as.character(reads$R1))
pool <- dada(derep, err=err, multithread=24, verbose=0)
saveRDS(pool, out)
saveRDS(derep, derep_out)