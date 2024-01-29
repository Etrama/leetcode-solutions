class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            temp = nums.count(i)
            if temp != 2:
                return i