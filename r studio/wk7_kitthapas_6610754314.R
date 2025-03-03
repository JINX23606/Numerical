ds <- read.csv(file.choose())
par(mar = c(4.5,4.4,4.1,1.9),xaxs="i",yaxs="i")

plot(x =ds$lnchprg,y=ds$staff,
     xlab="% of student in school lunch program",
     ylab=expression("staff per 1000 students"),
     xlim = c(0,100),ylim=c(0,200),bty="l",las=1,cex.axis=0.8,tcl=-0.2,pch=16,col="#fcbe03",cex=0.9)


