class Solution:
    def reverseWords(self, s: str) -> str:
        split_string = s.split()
        for index, word in enumerate(split_string):
            split_string[index] = word[::-1]
        return " ".join(split_string)
        


       