class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        flag = True
        og_word = word
        while flag:
            if word in sequence:
                count += 1
                word += og_word
            else:
                flag = False
        return count