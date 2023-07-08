class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for x in s:
            if x in s_dict.keys():
                s_dict[x] += 1
            else:
                s_dict[x] = 1
        for y in t:
            if y in t_dict.keys():
                t_dict[y] += 1
            else:
                t_dict[y] = 1
        return s_dict == t_dict
            