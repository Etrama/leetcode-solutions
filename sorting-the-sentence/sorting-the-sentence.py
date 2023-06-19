class Solution:
    def sortSentence(self, s: str) -> str:
        result_dict = {}
        for word in s.split():
            result_dict[int(word[-1])] = word[:-1]
        return " ".join(result_dict[j] for j in sorted(result_dict))