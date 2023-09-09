class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """ T(C) => O(logn) S(C) => O(1)"""
        if len(nums) == 0:
            return 0

        left, right = 0, len(nums)-1

        while left <= right:

            mid = left + (right - left) // 2 

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        
        return left
        
