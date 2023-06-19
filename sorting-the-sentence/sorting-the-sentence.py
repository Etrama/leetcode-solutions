class Solution:
    def sortSentence(self, s: str) -> str:
        result_dict = {}
        for word in s.split():
            result_dict[int(word[-1])] = word[:-1]
        result_dict = dict(sorted(result_dict.items()))
        return " ".join(result_dict.values())