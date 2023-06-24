class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        string = list(s)   
        left = 0
        right = len(string) - 1
        # print(ord("b") - ord("a")) #gives +1
        while left < right:
            if string[left] != string[right]:
                if ord(string[left]) - ord(string[right]) > 0:
                    string[left] = string[right]
                else:
                    string[right] = string[left]
            left += 1
            right -= 1  
        return "".join(string)