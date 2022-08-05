
import time

# fibonacci with dynaimc programming
def fib_cache(n=50, cache=None):
  
    if cache == None:
        cache = {}
        
    if n in cache:
        print(f"value of {n} in cache: {cache[n]}")
        return cache[n]
    
    if n < 2:
        return n 
        
    result = fib_cache(n-1, cache) + fib_cache(n-2, cache)
    print(f"value of result: {result}")
    
    cache[n] = result
    
    return result

print(fib_cache())
