# Logic: 
# Kadane's Algorithm - 
# maxSubArray(nums, i), which means the maxSubArray for nums[0:i] which must have nums[i] as the end element
# Relation -> maxSubArray(nums, i) = max(maxSubArray(nums, i-1) + nums[i], nums[i])
# Time Complexity - O(N), memory - O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_best_sum = nums[0]
        largest_sum = nums[0]
        for i in range(1, len(nums)):
            current_best_sum = max(nums[i], current_best_sum + nums[i])
            largest_sum = max(largest_sum, current_best_sum)
        
        return largest_sum