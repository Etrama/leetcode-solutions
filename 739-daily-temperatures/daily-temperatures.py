class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # the key to this problem I feel
        # is to figure out that we can append tuples to a stack
        # instead of just single values
        answer = len(temp)*[0]
        stack = []
        for index, val in enumerate(temp):
            while stack and stack[-1][1] < val:
                previous_index, previous_value = stack.pop()
                answer[previous_index] = index - previous_index
            stack.append((index, val))
        return answer