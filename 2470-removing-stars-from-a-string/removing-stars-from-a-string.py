class Solution:
    def removeStars(self, s: str) -> str:
        result_stack = []
        for character in s:
            if character == "*":
                result_stack.pop(-1)
            else:
                result_stack.append(character)
        return "".join(result_stack)