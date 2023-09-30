class Solution:     
    def isStrictlyPalindromic(self, num: int) -> bool:
        base_limit = num-1
        for base in range(2,base_limit):
            # convert number to the base needed
            # check if palindromic
            result_array = []
            while num != 0:
                result_array.insert(0,str(num%base))
                num = num / base
            check = "".join(result_array)=="".join(result_array[::-1])
            if not check:
                return False
        return True
