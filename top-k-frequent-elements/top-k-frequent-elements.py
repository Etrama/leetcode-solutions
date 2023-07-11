import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = collections.Counter(nums)
        print(count_dict)
        # print(sorted(count_dict, key=count_dict.get, reverse=True))
        return list(sorted(count_dict, key=count_dict.get, reverse=True))[:k]
        
        # reverse_count_dict = {v:k for k,v in count_dict.items()}
        # print(reverse_count_dict)
        # print(sorted(reverse_count_dict))
        # print(list(sorted(reverse_count_dict, key=reverse_count_dict.get,reverse=True)))
        # return list(sorted(reverse_count_dict, key=reverse_count_dict.get,reverse=True))[:k]

        
