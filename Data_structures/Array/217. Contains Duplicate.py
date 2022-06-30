# Logic: 
# Sort the array, iterate over the array if any two consecutive elements
# are same return True else return False
# Time Complexity - O(N log(N)), memory - O(1) (not counting the memory used to sort)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        output = False
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                output = True
                break
        return output