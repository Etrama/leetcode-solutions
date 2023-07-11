class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, val in enumerate(nums):
            if target-val in nums[idx+1:]:
                return idx, nums[idx+1:].index(target-val)+idx+1