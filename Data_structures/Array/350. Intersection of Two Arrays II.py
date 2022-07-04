# Logic: Two Pointer Approach
# Sort nums1 & nums2. Two pointers i and j pointing to index 0.
# If nums1[i] == nums2[j], append the element in intersection list else
# keep on incrementing the indices of the smaller element
# Time Complexity - O(max(N*log(N),  M*log(M)), memory - O(1)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                intersection.append(nums1[i])
                i += 1
                j += 1
        return intersection