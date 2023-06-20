class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        result = 0
        old_index = 0
        for char in word:
            new_index = keyboard.index(char)
            difference = abs(new_index - old_index)
            result += difference
            old_index = new_index
        return result 