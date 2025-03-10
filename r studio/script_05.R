data(trees)
summary(trees)
str(trees)

t.test(trees$Height,mu=70,conf.level=0.99)
wilcox.test(trees$Height,mu=70,alternative="less")

wage1 <- read.csv(file.choose())

t.test(wage1$wage ~ wage1$female,var.equal=TRUE)
tapply(wage1$wage,wage1$female,mean)
#  continuous variable หลายค่า  discrete น้อยค่า
tapply(wage1$wage,wage1$female,var)

var.test(wage1$wage ~ wage1$female)

wilcox.test(wage1$wage ~ wage1$female)
table(wage1$married,wage1$female)
A<-matrix(c(86,120,188,132),byrow=TRUE,nrow=2)
colnames(A) <- c("male","female")
rownames(A) <- c("single","married")
print(A)

chisq.test(A)
