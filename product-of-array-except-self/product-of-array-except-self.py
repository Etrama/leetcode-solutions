class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1]*len(nums)
        for i in range(1, len(nums)):
            left_products[i] = left_products[i-1]*nums[i-1]
        right_products = [1]*len(nums)
        for i in reversed(range(len(nums)-1)):
            right_products[i] = right_products[i+1]*nums[i+1]
        answer = []
        for j in range(len(nums)):
            answer.append(left_products[j]*right_products[j])
        return answer