class Solution:
    def makePalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        diff = 0
        while left < right:
            if s[left] != s[right]:
                diff += 1
            left+=1
            right-=1
        return diff<=2