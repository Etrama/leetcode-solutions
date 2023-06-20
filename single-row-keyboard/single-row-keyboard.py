class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        result = 0
        old_index = 0
        for char in word:
            new_index = keyboard.index(char)
            difference = new_index - old_index
            if difference < 0:
                difference = -1*difference
            result += difference
            old_index = new_index
        return result 