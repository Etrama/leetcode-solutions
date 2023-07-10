import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        small = string.ascii_lowercase
        big = string.ascii_uppercase
        numbers = "0123456789"
        big_to_small = dict(zip(big, small))
        s = list(s)
        for idx, val in enumerate(s):
            if val not in small and val in big:
                s[idx] = big_to_small[val]
            elif val not in small and val not in big and val not in numbers:
                s[idx] = ""
        s = "".join(s)
        return s == s[::-1]