class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) >= 2:
            temp = str(num)
            summation = 0
            for i in temp:
                summation += int(i)
            num = summation
        else:
            return num
