args <- commandArgs(TRUE)

# LOAD PARAMS
seqtab_nochim_rds <- readRDS(args[[1]])
seqtab_rds <- readRDS(args[[2]])

mergers <- readRDS(args[[3]])

derepR1 <- readRDS(args[[4]])
derepR2 <- readRDS(args[[5]])

dadaR1 <- readRDS(args[[6]])
dadaR2 <- readRDS(args[[7]])


read_tracking_loc <- c(args[[8]])

library(dada2)




getN <- function(x) sum(getUniques(x))

track <- cbind(sapply(derepR1, getN), sapply(derepR2, getN),sapply(dadaR1, getN), sapply(dadaR2, getN), sapply(mergers, getN), 
               rowSums(seqtab_nochim_rds))

colnames(track) <- c('derepR1', 'derepR2', "denoisedF", "denoisedR", "merged", "nonchim")

write.table(track, read_tracking_loc, sep='\t', col.names = NA, quote = FALSE)
