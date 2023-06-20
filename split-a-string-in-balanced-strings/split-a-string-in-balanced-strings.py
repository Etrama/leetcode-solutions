class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_result = 0
        running_count = 0
        for letter in s:
            if letter == "R":
               running_count += 1
            elif letter == "L":
                running_count -= 1
            if running_count == 0:
                count_result += 1
        return count_result