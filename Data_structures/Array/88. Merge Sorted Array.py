# Logic: 
# Traverse both the lists from the end towards the start. Compare both the lists
# at the end index and put the largest elements at the end of the first list.
# Time Complexity - O(m+n), memory - O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        while (i>=0 and j>=0):
            if nums1[i] < nums2[j]:
                nums1[i + j + 1] = nums2[j]
                j -= 1
            else:
                nums1[i + j + 1] = nums1[i]
                i -= 1
        while (i<0 and j>=0):
            nums1[i + j + 1] = nums2[j]
            j -= 1
        