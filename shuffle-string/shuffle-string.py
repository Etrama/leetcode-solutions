class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ref_dict = dict(zip(indices,s))
        print(ref_dict)
        ref_dict = sorted(ref_dict.items())
        result = ""
        for _, val in ref_dict:
            result += val
        return result