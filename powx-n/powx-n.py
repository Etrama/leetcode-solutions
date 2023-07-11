class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x*x
        if n > 2 and n%2 == 0:
            powern_by_2 = self.myPow(x, n/2)
            result = self.myPow(powern_by_2, 2)
            return result
        if n > 2 and n%2 == 1:
            result = x * self.myPow(x, n-1)
            return result
        
