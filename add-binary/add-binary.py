class Solution:
    def addBinary(self, a: str, b: str) -> str:
        temp = int(a,2) + int(b,2)
        return bin(temp)[2:]