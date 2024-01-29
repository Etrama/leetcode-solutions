class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, left, right = [], [1], [1]
        # left product calculation
        for i in range(len(nums)):
            if i != 0:
                left.append(left[-1]*nums[i-1])
        for i in range(len(nums)-1,-1,-1):
            if i != len(nums)-1:
                right.append(right[-1]*nums[i+1])
        right = right[::-1]
        for i, j in zip(left, right):
            ans.append(i*j)
        return ans
            
        