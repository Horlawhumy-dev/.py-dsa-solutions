def binary_search(low, high, find_position):

    while low <= high:
        mid = (low + high) // 2

        position = find_position(mid)

        if position == "found":
            return mid
        elif position == "right":
            low = mid + 1
        elif position == "left":
            high = mid -1
    
    return -1

def find_first_position(nums, target):

    def find_position(mid):

        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return "left"
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left" 

    return binary_search(0, len(nums)-1, find_position)

def find_last_position(nums, target):

    def find_position(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return "right"
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left" 
    return binary_search(0, len(nums)-1, find_position)

def searchRange(nums: list, target: int) -> list:
    """
        nums: list of sorted numbers,
        target: number to find its position of first and last occurences
    """
    return [find_first_position(nums, target), find_last_position(nums, target)]
