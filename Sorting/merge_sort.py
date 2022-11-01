
def merge_sort(nums: list[int]) -> list[int]:

    if len(nums) <= 1:
        return nums

    mid  = len(nums) // 2

    left_nums = nums[:mid]
    right_nums = nums[mid:]

    left_sorted = merge_sort(left_nums)
    right_sorted = merge_sort(right_nums)

    return merge(left_sorted, right_sorted)

def merge(list1: list[int], list2: list[int]) -> list[int]:

    list3 = list()
    i, j = 0, 0

    while i <= len(list1)-1 and j <= len(list2)-1:
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i += 1
        else:
            list3.append(list2[j])
            j += 1

    return list3 + list1[i:] + list2[j:]