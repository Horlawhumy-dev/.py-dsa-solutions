
def binary_search(nums, low, high, condition):

    while low <= high:
        mid = (low + high) // 2

        type = condition(mid)

        if type == "found":
            return nums[mid]
        elif type == "left":
            high = mid -1
        else:
            low = mid + 1


def find_rotation_count(nums):

    if len(nums) == 1:
        return nums[0]

    def condition(mid):
        high = len(nums)-1
    
        if nums[mid] < nums[mid-1]:
            return "found"
        elif nums[mid] < nums[high]:
            return "left"
        else:
            return "right"
    return binary_search(nums, 0, len(nums)-1, condition)

print(find_rotation_count([2,]))