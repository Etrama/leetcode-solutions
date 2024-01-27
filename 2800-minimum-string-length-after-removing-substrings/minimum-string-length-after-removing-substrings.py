class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            cond1 = len(stack) != 0 and (stack[-1] == "A" and char =="B")
            cond2 = len(stack) != 0 and (stack[-1] == "C" and char == "D")
            if cond1 or  cond2:
                stack.pop(-1)
            else:
                stack.append(char)
        return len(stack)