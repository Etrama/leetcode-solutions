class Solution:
    def isValid(self, s: str) -> bool:
        open_close_map = {"(":")",
                        "[":"]",
                        "{":"}"}
        open_set = {"(","{","["}
        stack = []
        for i in s:
                if i in open_close_map.keys():
                    stack.append(i)
                elif i in open_close_map.values() and len(stack) > 0:
                    if i == open_close_map[stack[-1]]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0
