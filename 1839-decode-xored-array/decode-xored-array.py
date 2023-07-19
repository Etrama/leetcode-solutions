class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first,]
        for elem in encoded:
            arr.append(arr[-1]^elem)
        return arr