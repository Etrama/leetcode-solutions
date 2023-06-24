class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = len(words)
        for word in words:
            for letter in word:
                if letter not in allowed:
                    count-= 1
                    break
        return count