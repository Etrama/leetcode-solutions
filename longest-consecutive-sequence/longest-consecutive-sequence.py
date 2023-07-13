class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums = sorted(nums)
        current_count = 0
        max_count = 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                current_count += 1
                if current_count > max_count:
                    max_count = current_count
            elif nums[i+1] == nums[i]:
                pass
            else:
                current_count = 0
        return max_count+1