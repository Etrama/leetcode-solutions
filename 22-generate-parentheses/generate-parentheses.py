class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        # init = "("
        stack.append("(")
        def add_open(current):
            if current.count("(") < n:
                current += "("
                stack.append(current)
        def add_close(current):
            close_count = current.count(")")
            if close_count < current.count("("):
                # and close_count < n - condition not needed, handled by open
                current += ")"
                stack.append(current)
        while stack:
            contender = stack.pop()
            if len(contender) != 2*n:
                add_open(contender)
                add_close(contender)
            else:
                result.append(contender)
        return result