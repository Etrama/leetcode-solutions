class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_sent_length = 0
        for sentence in sentences:
            temp = sentence.count(" ") + 1
            if temp > max_sent_length:
                max_sent_length = temp
        return max_sent_length