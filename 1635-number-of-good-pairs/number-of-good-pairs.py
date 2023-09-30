class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_pairs = 0
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if nums[i] == nums[j] and i<j:
                    num_pairs+=1
        return num_pairs