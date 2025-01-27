num <- 2.2
class(num)
char <- "hello"
class(char)
logi <- TRUE
class(logi)
is.numeric(num)
is.character(char)
is.logical(logi)

num_char <- as.character(num)
num_char
class(num_char)
class(char)
char_num <- as.numeric(char)

my_mat <- matrix(1:16,nrow = 4,byrow = TRUE)
my_mat2 <- matrix(1:16,nrow = 4,byrow = FALSE)
my_array <- array(1:16,dim=c(2,4,2))
rownames(my_mat) <- c("A","B","C","D")
colnames(my_mat) <- c("a","b","c","d")
my_mat_t <- t(my_mat)
my_mat_diag <- diag(my_mat)

mat.1 <- matrix(c(2,0,1,1),nrow = 2)
mat.2 <- matrix(c(1,1,0,2),nrow = 2)
mat.1 + mat.2
mat.1 * mat.2
mat.1 %*% mat.2
list_1 <- list(c("black","yellow","orange"),
               c(TRUE,TRUE,FALSE,TRUE,FALSE,FALSE),
               matrix(1:6,nrow = 3))
list_2 <- list(colors = c("black","yellow","orange"),
               evaluation = c(TRUE,TRUE,FALSE,TRUE,FALSE,FALSE),
               times = matrix(1:6,nrow = 3))

p.height <- c(180,155,160,167,181)
p.weight <- c(65,50,52,58,70)
p.names <- c("John","Bob","Wlliam","Mike","Mille")
df <- data.frame(name=p.names,height=p.height,weight = p.weight)

wage_1 <- read.csv(file.choose())
View(wage_1)
