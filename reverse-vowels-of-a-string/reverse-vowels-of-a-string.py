class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 1:
            return s
        vowels = "aeiouAEIOU"
        s = list(s)
        left = 0
        right = len(s)-1
        # print(s)
        while left < right:
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1
            if s[left] in vowels and s[right] in vowels:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1
        return "".join(s)