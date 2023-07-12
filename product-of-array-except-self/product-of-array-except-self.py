class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1]
        for i in range(1, len(nums)):
            left_products.append(left_products[-1]*nums[i-1])
        right_products = [1]
        k = len(nums)-1
        while k >= 1:
            right_products.insert(0, right_products[0]*nums[k])
            k -= 1
        print(left_products)
        print(right_products)
        answer = []
        for j in range(len(nums)):
            answer.append(left_products[j]*right_products[j])
        return answer