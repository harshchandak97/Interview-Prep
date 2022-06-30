# Logic: 
# Create a set, add elements to it. If an element is already present in
# the set return True else return False
# Time Complexity - O(N), memory - O(N) (created a set)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        output = False
        number_set = set()
        for element in nums:
            if element in number_set:
                output = True
                break
            else:
                number_set.add(element)    
        return output