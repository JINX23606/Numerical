wage_1 <- read.csv(file.choose())
summary(wage_1[,1:7])
xtabs(~ educ + female,data = wage_1)
xtabs(~ wage + female,data = wage_1)
tapply(wage_1$wage,wage_1$female,mean)
aggregate(wage_1[,1:4],by = list(female = wage_1$female),FUN = mean)
aggregate(wage_1[,1:4],by = list(female = wage_1$female,married = wage_1$married),FUN = mean)
#export data
wage_df_2 <-wage_1[order(wage_1$female,wage_1$wage),]
wage_df_2$wage_sqrt <- sqrt(wage_df_2$wage)

plot(wage_1$wage)
plot(wage_1$educ,y=wage_1$wage)


plot(wage_1$tenure,y=wage_1$wage)


x <- 1:10
y <- seq(from = 1,to = 20,by=2)
#fig axes
par(mfrow =c(2,2))
plot(x,y,type = "l")
plot(x,y,type = "b")
plot(x,y,type = "o")
plot(x,y,type = "c")

hist(wage_1$wage)
par(mfrow = c(1,1))

brk <- seq(from  = 0 ,to = 25 , by = 1)
hist(wage_1$wage,breaks=brk)


dens <- density(wage_1$wage)
hist(wage_1$wage,breaks=brk,main = "Hourly Wage",freq = FALSE)
lines(dens)

boxplot(wage_1$wage,ylab="Hourly Wage (USD)")

boxplot(wage ~ female*married,data = wage_1,ylab="Hourly Wage(USD)",xlab="Males and Females")
