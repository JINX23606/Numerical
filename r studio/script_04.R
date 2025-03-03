#4.3.1 Customising with arguments in text book
wage1 <- read.csv(file.choose())
par(mar = c(4.1,4.4,4.1,1.9),xaxs="i",yaxs="i")

plot(x =wage1$exper,y=wage1$wage,
     xlab="experience (years)",
     ylab=expression("hourly wage (usd "/" hour)"),
    xlim = c(0,60),ylim=c(0,30),bty="l",las=1,cex.axis=0.8,tcl=-0.2,pch=16,col="#FE0000",cex=0.9)
text(x=55,y=28,label="wage 1",cex=2)
#las = 1 rotate ylabel ,tcl = dash line in the ax 






#6.1 One and two sample tests