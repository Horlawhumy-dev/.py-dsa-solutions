
def task(nums) -> int:
    for i in range(len(nums)):
        if i % 2 == 0 and nums[i] % 2 == 0:
            return nums[i]
            
        if i % 2 != 0 and nums[i] % 2 != 0:
            return nums[i]
    return -1
