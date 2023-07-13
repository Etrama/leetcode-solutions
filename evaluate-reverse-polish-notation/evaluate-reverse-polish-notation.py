class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","-","*","/"}
        stack = []
        for token in tokens:
            if token in operators:
                y = int(stack.pop())
                x = int(stack.pop())
                if token == "+":
                    stack.append(x+y)
                elif token == "-":
                    stack.append(x-y)
                elif token == "*":
                    stack.append(x*y)
                else:
                    stack.append(x/y)
            else:
                stack.append(token)
        return int(stack[0])
                