class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ref_dict = {}
        attempt = ""
        for x, y in zip(s, t):
            if x not in ref_dict.keys():
                if y not in ref_dict.values():
                    ref_dict[x] = y
                else:
                    ref_dict[x] = "0"
            attempt += ref_dict[x]
        return attempt == t