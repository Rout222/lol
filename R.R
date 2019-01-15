library(latticeExtra)
dados <- read.table("querydumpgraph.csv",
            header=TRUE,
            sep=",",
            colClasses=c(rep("numeric",2)),
          na="?")

y  = as.numeric(unlist(dados[1]))
x = as.numeric(unlist(dados[2]))

dados=data.frame(x,y)
xyplot(x ~ y, dados, type = "l" , lwd=2, xlab = "peso", ylab = "n",
       auto.key=list(space="top", columns=4, 
                     title="Databases", cex.title=9,
                     lines=TRUE, points=FALSE))
