class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(sentence.count(" ") for sentence in sentences) + 1