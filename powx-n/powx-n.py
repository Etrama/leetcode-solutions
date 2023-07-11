class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.binary_power(x, n)
    
    def binary_power(self, x, n):
        if n < 0:
            return self.binary_power(1/x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x*x
        if n > 2 and n%2 == 0:
            powern_by_2 = self.binary_power(x, n/2)
            result = self.binary_power(powern_by_2, 2)
            return result
        if n > 2 and n%2 == 1:
            result = x * self.binary_power(x, n-1)
            return result
        
