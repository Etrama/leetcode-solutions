import collections
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ref = collections.Counter(nums)
        result = [i for i in ref.values() if i >1]
        if len(result) == 0:
            return False
        return True