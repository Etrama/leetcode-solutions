class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ref_dict = {"}":"{", "]":"[", ")":"("}
        for bracket in s:
            if bracket in ["(", "[", "{"]:
                stack.append(bracket)
            else:
                if len(stack)!=0 and ref_dict[bracket] == stack[-1]:
                    stack.pop(-1)
                    continue
                else:
                    return False
        return len(stack) == 0
