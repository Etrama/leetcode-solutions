class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while True:
                j = i + 1
                if j < len(nums) and nums[i] == nums[j]:
                    del nums[j]
                else:
                    break
            