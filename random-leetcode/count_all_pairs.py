def count_pairs_with_sum_divisible_by_x(price, x):
    """
      Amazon is offering a discount on every purchase of a pair of products whose price sum is divisible by x. 
      Given the price of n products in the store, find the number of pairs(i, j) where i < j and price[i] + price[j] is divisible by x. For example, n = 5 products, x = 60, and price = [31. 25, 85, 29, 35]
    """
    remainder_count = {}  # Dictionary to store the count of each remainder modulo x
    count = 0  # Initialize the count of valid pairs to 0

    for p in price:
        remainder = p % x  # Calculate the remainder of the current price
        complement_remainder = (x - remainder) % x  # Calculate the remainder needed to sum to x

        # Count the number of prices that have the complement_remainder as their remainder
        count += remainder_count.get(complement_remainder, 0)
    
        # Update the remainder_count dictionary
        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

    return count
    
print(count_pairs_with_sum_divisible_by_x([3, 7, 27, 23], 10))
