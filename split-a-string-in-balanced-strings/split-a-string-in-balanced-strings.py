class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_result = 0
        count_r = 0
        count_l = 0
        for letter in s:
            if letter == "R":
                count_r += 1
            elif letter == "L":
                count_l += 1
            if count_r == count_l and count_r != 0 and count_l != 0:
                count_result += 1
                count_r = 0
                count_l = 0
        return count_result