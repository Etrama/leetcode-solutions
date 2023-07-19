class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2, reverse=True)
        result = 0
        for i, j in zip(nums1, nums2):
            result += i*j
        return result