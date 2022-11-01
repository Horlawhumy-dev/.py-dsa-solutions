
def quick_sort(nums):

    if len(nums) <= 1:
        return nums

    pivot = partition(nums, len(nums)-1)

    return quick_sort(nums[:pivot]) + quick_sort(nums[pivot:])



def partition(nums, pivot):
    i, j = 0, pivot-1

    while j > i:
        if nums[i] <= nums[pivot]:
            i += 1
        elif nums[j] > nums[pivot]:
            j -= 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
    
    if nums[i] > nums[pivot]:
        nums[i], nums[pivot] = nums[pivot], nums[i]
        return i 
    else:
        return pivot

print(quick_sort([2, 1, 4, 3, 6, 9, 3, 0]))