dados <- read.table("Rquery.csv",
                    header=TRUE,
                    sep=",",
                    colClasses=c("character",rep("numeric",5), "character", "numeric", "character", "character"),
                    na="?")