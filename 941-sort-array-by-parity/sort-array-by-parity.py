class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                temp = nums[i]
                del nums[i]
                nums.insert(0,temp)
        return nums