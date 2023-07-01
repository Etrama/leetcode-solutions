class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new = []
        middle = len(nums) // 2
        for i in range(len(nums)//2):
            new.append(nums[i])
            new.append(nums[middle])
            middle+=1
        return new