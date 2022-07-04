# Logic: 
# Create an empty dictionary. Iterate over all the elements in the list.
# Say that the current element is xa. For current element, xa we look at the
# previous values stored in the dictionary and try to find if there exists an
# element target - xa (i.e. xb) - Return the indices of both the elements.
# Time Complexity - O(N), memory - O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_dictionary = {}
        for i in range(len(nums)):
            if (target - nums[i]) in number_dictionary:
                return [i, number_dictionary[target - nums[i]]]
            else:
                number_dictionary[nums[i]] = i
