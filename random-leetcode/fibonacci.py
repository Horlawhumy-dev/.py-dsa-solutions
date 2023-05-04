
import time

# fibonacci with dynaimc programming(memoization)
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

    
  
 #dynamic programming method(bottom-up)
def fibonacci_btm_up(n=10):
    result_so_far = [0, 1]
    
    for i in range(2, n+1):
        print(result_so_far)
        result_so_far.append(result_so_far[i-1] + result_so_far[i-2])
    return result_so_far[n]
    
print(fibonacci_btm_up())
