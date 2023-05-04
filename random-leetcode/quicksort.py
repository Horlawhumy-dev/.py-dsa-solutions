def quicksort(arr = [3, 2, 4, 1]):
   
    if len(arr) <= 1:
        return arr
        
    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    
    middle = [x for x in arr if x == pivot]
    
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)
    
    
print(quicksort())
