library(dada2)

fs_prefix <- '/data11/bio/mg_data'
df <- 'GOS_DETI'
sample_set <- 'run_id__B2'

# LOAD SEQTAB
seqtab_rds_loc = paste(fs_prefix,df,'dada2',sample_set,'learn_erros__def/seqtab_nochim__20.rds', sep='/')
seqtab_rds_tsv = paste(fs_prefix,df,'dada2',sample_set,'learn_erros__def/seqtab_nochim__20.tsv', sep='/')

seqtab <- readRDS(seqtab_rds_loc)
# rename FUCKING rows
rownames(seqtab) <- gsub('.{3}$', '', sapply(strsplit(rownames(seqtab), ".", fixed = TRUE), `[`, 1))
write.table(seqtab,seqtab_rds_tsv, sep='\t', col.names = NA,quote = F)


# load taxa
taxa_rds_loc = paste(fs_prefix,df,'dada2',sample_set,'learn_erros__def/taxa_20.rds', sep='/')
taxa_tsv_loc = paste(fs_prefix,df,'dada2',sample_set,'learn_erros__def/taxa_20.tsv', sep='/')
taxa <- readRDS(taxa_rds_loc)
write.table(taxa,taxa_tsv_loc, sep='\t', col.names = NA,quote = F)



### READS TRACKING
mergers_loc = paste(fs_prefix, df, 'dada2',sample_set,'learn_erros__def/mergers__20.rds', sep = '/')
mergers <- readRDS(mergers_loc)

derepR1_loc = paste(fs_prefix, df, 'dada2',sample_set,'learn_erros__def/derepR1.rds', sep = '/')
derepR2_loc = paste(fs_prefix, df, 'dada2',sample_set,'learn_erros__def/derepR2.rds', sep = '/')
derepR1 <- readRDS(derepR1_loc)
derepR2 <- readRDS(derepR2_loc)

dadaR1_loc = paste(fs_prefix, df, 'dada2',sample_set,'learn_erros__def/dadaR1.rds', sep = '/')
dadaR2_loc = paste(fs_prefix, df, 'dada2',sample_set,'learn_erros__def/dadaR2.rds', sep = '/')
dadaR1 <- readRDS(dadaR1_loc)
dadaR2 <- readRDS(dadaR1_loc)

seqtab_rds_loc = paste(fs_prefix,df,'dada2',sample_set,'learn_erros__def/seqtab__20.rds', sep='/')
seqtab <- readRDS(seqtab_rds_loc)

seqtab_nochim_rds_loc = paste(fs_prefix,df,'dada2',sample_set,'learn_erros__def/seqtab_nochim__20.rds', sep='/')
seqtab.nochim <- readRDS(seqtab_nochim_rds_loc)

getN <- function(x) sum(getUniques(x))

track <- cbind(sapply(derepR1, getN), sapply(derepR2, getN),sapply(dadaR1, getN), sapply(dadaR2, getN), sapply(mergers, getN), 
               rowSums(seqtab.nochim))

colnames(track) <- c('derepR1', 'derepR2', "denoisedF", "denoisedR", "merged", "nonchim")

read_tracking_loc = paste(fs_prefix,df,'dada2',sample_set,'learn_erros__def/track.tsv', sep='/')
write.table(track, read_tracking_loc, 
            sep='\t', col.names = NA, quote = FALSE)
