class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        combined = []
        for i in range(len(word1)):
            if len(word1) != 0:
                combined.append(word1.pop(0))
            if len(word2) != 0:
                combined.append(word2.pop(0))
        if len(word1) != 0:
            combined.extend(word1)
        if len(word2) != 0:
            combined.extend(word2)
        return "".join(combined)
