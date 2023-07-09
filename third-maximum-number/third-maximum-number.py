class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = max(nums)
        nums.remove(first_max)
        while len(nums)!=0 and max(nums) == first_max:
            nums.remove(first_max)
            # remove multiple occurences of max
        if len(nums) != 0:
            second_max = max(nums)
            nums.remove(second_max)
            while len(nums)!=0 and max(nums)==second_max:
                nums.remove(second_max)
            # remove multiple occurences of this as well
        if len(nums) != 0:
            third_max = max(nums)
            return third_max
        return first_max