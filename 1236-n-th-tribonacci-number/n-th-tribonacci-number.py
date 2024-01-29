class Solution:
    def tribonacci(self, n: int) -> int:
        ref = [0,1,1]
        if n <= 2 and n >= 0:
            return ref[n]
        else:
            for i in range(n-3):
                next = sum(ref)
                ref.append(next)
                del ref[0]
            # print(ref)
        return sum(ref)