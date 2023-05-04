
def is_possible(a=1, b=1, c=5, d=3):
    """
        Returns a string value of "YES" or "NO" whether c and d can be generated from a and b.
        @params : a and b are init values - while c and d are final generated values if true.
        @returns : string of "YES" or "NO"
    """
    
    while a <= c and b <= d:
        if a == c and b == d:
            return "YES"
        temp = c
        c = get_val_c(c, d)
        d = get_val_d(d, temp)
    return "NO"
        
def get_val_c(c, d):
    c2 = lambda c, d: c - d if c > d else c
    return c2(c, d)
   
def get_val_d(d, temp):
    d2 = lambda d, temp: d - temp if d > temp else d
    return d2(d, temp)

print(is_possible())
