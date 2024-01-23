class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict = {}
        for num in arr:
            if num not in count_dict:
                count_dict[num] = arr.count(num)
        trial = count_dict.values()
        return len(list(trial)) == len(set(trial))