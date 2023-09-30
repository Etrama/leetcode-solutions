class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        solution = []
        for i in nums:
            if i%2 == 0:
                solution.insert(0,i)
            else:
                solution.append(i)
        return solution