class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        og_word = word
        while word in sequence:
            count += 1
            word += og_word
        return count