class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        split_s = s.split(" ")
        result = split_s[:k]
        return " ".join(result)