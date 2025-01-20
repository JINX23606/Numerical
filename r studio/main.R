4^2
pi
log(exp(1)) #log_e
log10(1) 
exp(2) #e^()
sqrt(4)
a <- 10 # <- equal 
b <- 20
a+b
my_obj <- 48
my_obj

area_circle <- pi*(20/2)^2
area_circle

(14*.51)^(1/3)

my_obj2 <- "R is cool"
my_obj2 <- 1024

my_obj3 <- my_obj+ my_obj2
my_obj3

char_obj <- "hello"
char_obj2 <- "world"
char_obj3 <- char_obj & char_obj2

my_vec <- c(2,3,1,6,4,3,3,7) #array aka list
mean(my_vec)
var(my_vec)
sd(my_vec)
length(my_vec)

my_seq <- 1:10
my_seq
my_seq2 <- 10:1
my_seq2 <- seq(from =1 ,to = 5,by = .5)
#Replicate
my_seq3 <- rep(2,time=10)
my_seq3
my_seq4 <- rep("abc",time=3)
my_seq4
my_seq5 <- rep(1:5,times=3)
my_seq5
my_seq6 <- rep(1:5,each=3)
my_seq6
my_seq7 <- rep(c(3,1,10,7),each =3)
my_seq7

in_vec <- c(3,1,10,7)
my_seq7 <- rep(in_vec,each =3)
my_seq7

rep(c(1,2,3),times = 3)
rep(c("a","e","e","g"),each =3)
rep(1:3,each=3,times=2)

my_vec[3]
val_3 <- my_vec[3]
my_vec[c(1,5,6,8)]
my_vec[3:8]
my_vec[my_vec >4]
my_vec > 4 
my_vec[c(FALSE,FALSE,FALSE,TRUE,FALSE,FALSE,FALSE,TRUE)] 
my_vec[my_vec >=4]
my_vec[my_vec < 4]
my_vec[my_vec <= 4]
my_vec[my_vec == 4]
my_vec[my_vec != 4]

val26 <- my_vec[my_vec <6 & my_vec >2]
val26
val63 <- my_vec[my_vec >6 | my_vec<3]
val63
my_vec[4] <- 500
my_vec[my_vec%%2!=0] <- 500
my_vec[c(6,7)]<-100
my_vec
my_vec[my_vec<=4] <- 1000
my_vec
vec_sort <- sort(my_vec)
vec_sort
vec_sort2 <- sort(my_vec,decreasing = TRUE)
vec_sort2
vec_sort3 <- rev(sort(my_vec))
vec_sort3

my_vec2 <- c(3,5,7,1,9,20)
my_vec2*5
my_vec3 <- c(17,15,13,19,11,0)
my_vec2 + my_vec3
my_vec2 * my_vec3
my_vec4 <- c(1,2)
my_vec2 + my_vec4
temp <- c(7.2,NA,7.1,6.9,6.5,5.8,5.8,5.5,NA,5.5)
temp
mean_temp <- mean(temp)
mean_temp
