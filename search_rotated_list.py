class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[low]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid -1

        return -1

cls = Solution()
print(cls.search([4,5,6,7,0,1,2], 21))