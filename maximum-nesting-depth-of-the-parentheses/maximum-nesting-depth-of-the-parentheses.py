class Solution:
    def maxDepth(self, s: str) -> int:
        max_opens = 0
        current_max_opens = 0
        for letter in s:
            if letter == "(":
                current_max_opens += 1
            if letter == ")":
                max_opens = max(max_opens, current_max_opens)
                current_max_opens -= 1
        # print(max_opens)
        return max_opens