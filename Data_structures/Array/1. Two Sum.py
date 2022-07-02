# Logic: 
# Brute Force - 
# Two for loops - i and j position of the two elements.
# Check if nums[i] + numbs[j] == target, if yes return [i, j]
# Time Complexity - O(N^2), memory - O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
