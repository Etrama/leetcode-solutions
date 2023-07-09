class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        reference = set([i+1 for i in range(len(nums))])
        nums = set(nums)
        return reference.difference(nums)