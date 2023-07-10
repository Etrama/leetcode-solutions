import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = collections.Counter(nums)
        return max(count_dict, key=count_dict.get)