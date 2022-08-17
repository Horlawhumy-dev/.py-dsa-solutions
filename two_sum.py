class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        
        if len(nums) == 0:
            return []
        
        store = {}
        result = []
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in store:
                result.append(store[diff])
                result.append(i)
            else:
                store[nums[i]] = i
        return result
