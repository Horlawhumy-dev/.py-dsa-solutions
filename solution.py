
def is_possible(a=1, b=1, c=5, d=2):
    """
        Returns a string value of "YES" or "NO" whether c and d can be generated from a and b.
        @params : a and b are init values - while c and d are final generated values if true.
        @returns : string of "YES" or "NO".
    """
    # a=1, b=1, c=5, d=2 "YES"
    # a=1, b=1, c=3, d=2
    # a=1. b=1, c=1, d=2
    # a=1, b=1, c=1, d=1

    # a=1, b=2, c=4, d=1 "NO"
    # a=1 b=2 c=3 d=1
    # a=1, b=2, c=2, d=1
    # a=1 b=2, c=1 d=1

    while a <= c and b <= d:
        if a == c and b == d: # since i want to decrease c and d back to a and b
            return "YES"
        temp = c #holds initial value of c before decrement 
        c = reduce_c(c, d)
        d = reduce_d(d, temp)
    return "NO"
        
def reduce_c(c, d):
    reduced_c = lambda c, d: c - d if c > d else c
    return reduced_c(c, d) # returns 3 initially
   
def reduce_d(d, temp):
    reduced_d = lambda d, temp: d - temp if d > temp else d
    return reduced_d(d, temp)

print(is_possible())

# 1, 1, 5, 2

# temp = 5
# reduce_c(5, 2) - 3 #init vals
# reduce_d(2, 5) - 2

# temp = 3
# reduce_c(3, 2) - 1
# reduce_d(2, 3) - 2

# temp = 1
# reduce_c(1, 2) - 1
# reduce_d(1, 1) - 1

# a, b => a+b, b first
# a, b => a, a+b second

# # c, d from a, b

# 1, 1 => 5, 2

# 1, 1 => 1, 1+1 => 1, 2 => 2+1, 2 => 3, 2 => 3+2, 2 => 5, 2
