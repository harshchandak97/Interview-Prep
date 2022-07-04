# Logic: Dictionary
# Create a dictionary of elements in nums1 (or nums2 whichever is smaller),
# such that key = element, value = frequency of the element. Iterate over the
# other list and check if the element is present in the dictionary and value of
# the element is not equal to 0. If True, add the element into intersection list.
# Time Complexity - O(max(M, N), memory - O(min(M, N))

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums1_dict = {}
        for element in nums1:
            if element in nums1_dict:
                nums1_dict[element] += 1
            else:
                nums1_dict[element] = 1
                
        for number in nums2:
            if number in nums1_dict and nums1_dict[number] != 0:
                intersection.append(number)
                nums1_dict[number] -= 1
                
        return intersection