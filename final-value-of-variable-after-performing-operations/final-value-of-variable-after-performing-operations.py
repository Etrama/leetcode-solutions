class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        for element in operations:
            if "++" in element:
                value += 1
            else:
                value -= 1
        return value