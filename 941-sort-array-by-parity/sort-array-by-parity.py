class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     if nums[i] % 2 == 0:
        #         nums.insert(0,nums[i])
        #         del nums[i+1]
        # return nums
        nums.sort(key = lambda x: x%2)
        return nums