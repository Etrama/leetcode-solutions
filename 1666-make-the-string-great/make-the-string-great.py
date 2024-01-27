class Solution:
    def makeGood(self, s: str) -> str:
        # print(ord("a")-ord("A"),ord("b")-ord("B"))
        stack = []
        for i in range(len(s)):
            if stack and ((ord(stack[-1]) - ord(s[i]) == -32) or (ord(stack[-1]) - ord(s[i]) == 32)):
                stack.pop(-1)
            else:
                stack.append(s[i])
        return "".join(stack)