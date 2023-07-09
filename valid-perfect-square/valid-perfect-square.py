class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        squares = 1
        increment = 3
        while squares < num:
            squares = squares + increment 
            increment += 2
        return squares == num
