class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i in s:
            if i != "#":
                stack1.append(i)
            else:
                if len(stack1) != 0:
                    stack1.pop(-1)
        for j in t:
            if j != "#":
                stack2.append(j)
            else:
                if len(stack2) != 0:
                    stack2.pop(-1)
        return stack1 == stack2
