args <- commandArgs(TRUE)

fnFs <- c(args[[1]])
filtFs <- c(args[[2]])

truncLenF <- as.integer(args[[3]])
trimLeftF <- as.integer(args[[4]])
maxEEF <- as.numeric(args[[5]])
truncQ <- as.integer(args[[6]])
maxN <- as.integer(args[[7]])


library(dada2)

out <- filterAndTrim(fnFs, filtFs, truncLen=truncLenF, trimLeft=trimLeftF,
              maxN=maxN, maxEE=maxEEF, truncQ=truncQ, rm.phix=TRUE, compress=TRUE, minLen = 50)
print(out)