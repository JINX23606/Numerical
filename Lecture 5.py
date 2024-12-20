#============================================================================
# 5.1 Structure & Calling
#============================================================================
#
# 5.1.1 Single Output
def square(x):
    """
    Calculates the square of a given number.
    Arguments (Parameters):
        x: A scalar value (int or float)
    Returns:
        square: The square of the input number
    """
    output = x**2
    return output

# Calling
result = square(2)
print(f"The square of 2 is {result}")

# Matters of Docstring
help(square)

# ---------------------------------------
def f():
    print('1')

f()
#---------------------------------------
def sim_cd(K,L):
    """
    A very simple version of Cobb-Douglas Production Function.
    Parameters:
        K: Physical capital (float or int)
        L: Labor input (float or int)
        z: Total Factor Productivity (normalised 1)
        alpha: Output elasticity with respect to capital (set = 0.33)
    Returns:
        Y: Output produced (float)
    """ 
    z,  alpha = 1, 0.33
    Y = z * K**alpha * L**(1-alpha)
    return Y

sim_cd(1,2)
result = sim_cd(1,2)
print(f"Output (Y): {result}")
print(f"Output (Y): {result:.2f}")

# 5.1.2 Multiple Outputs

def test():
    return 'abc', 100

result = test()
print(result) 
type(result)    
result[0]    
result[1]
# we can unpack the multiple values and assign them to seperate variables
a,b = test()
print(a)
print(b)

# Marginal Product of Capital, Labor
def marginal_products(K,L):
    """
    Computes the marginal products of capital (MPK) and labor (MPL) for a 
    Cobb-Douglas production function.
    Parameters:
        K (float): Capital input.
        L (float): Labor input.
    Returns:
        tuple: (MPK, MPL) - Marginal product of capital and labor.
    """
    z = 1  # Total factor productivity
    alpha = 0.33  # Capital share
    MPK = z * alpha * K**(alpha - 1) * L**(1 - alpha)
    MPL = z * (1 - alpha) * K**alpha * L**(-alpha)
    return MPK, MPL

mpk, mpl = marginal_products(1,2)
print(f"Marginal Product of Capital (MPK) : {mpk:.2f}")
print(f"Marginal Product of Capital (MPL) : {mpl:.2f}")

#============================================================================
# 5.2 Scope of Variables
#============================================================================
# Key Points ---> Global Variables  vs. Local Variables
#            ---> 'global' keyword,
#            ---> name conflicts
s = 5  # Global variable
t = 7  # Global variable
def my_fun(u):
    x = s + u          # `x` is a local variable
    t = 2              	# Local variable `t` (shadows global `t`)
    global y            # Declare `y` as a global variable
    y = 2              	# Assign value to global `y`
    z = t + x + y      # `z` is a local variable
    return z
# Call the function
my_fun(1)
# Print statements to test variable scope
print(s)  # Output: 5 (global variable)
print(t)  # Output: 7 (global variable, unaffected by local`t`in my_fn)
print(y)  # Output: 2 (global variable, modified inside the function)
#print(u)  # Error: `u` is a local variable
#print(x)  # Error: `x` is a local variable
#print(z)  # Error: `z` is a local variable

# ===========================================================================
# 5.3 Reusing Functions
# ===========================================================================
#
# (i) Simple Illustration
def square(x):
    return x**2

def double_square(x):
    return 2 * square(x)

print(square(3))
print(double_square(3))

# (ii) Econ Application: MRTS
def mrts(K,L):
    mpk, mpl = marginal_products(K,L)
    ratio    = mpl/mpk
    return -1*ratio

result = mrts(1, 2)
print(f"MRTS: {result:.2f}")

#=============================================================================
# 5.4 Positional Arguments, Default Values,  and Keyword Arguments
#=============================================================================

# 5.4.1 Positional Arguments
def gen_cobb_douglas(z,K,L,alpha,beta):
    Y = z * K**alpha * L**beta
    return Y
gen_cobb_douglas(1,1,2,0.5,0.5)
gen_cobb_douglas(1,2,1,0.5,0.5)

# 5.4.2 Default Values
#
# Set default values: z = 1, alpha = 0.33, beta = 0.67
def gen_cobb_douglas_v2(K,L,z=1,alpha=0.33,beta=0.67):
    Y = z * K**alpha * L**beta
    return Y

gen_cobb_douglas_v2(2,3)            #K=2, L=3  ;  z, alpha, beta by default
gen_cobb_douglas_v2(2,3,2)          #K=2, L=3, z=2; alpha, beta by default
gen_cobb_douglas_v2(2,3,1,0.33,0.5)  #K=2, L=3, beta=0.5; z, alpha, by default

# 5.4.3 Keyword Arguments

gen_cobb_douglas_v2(2,3,beta = 0.5) # == gen_cobb_douglas_v2(2,3,1,0.33,0.5)