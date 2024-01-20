class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        current_vowels = []
        s_list = list(s)
        for letter in s_list:
            if letter in vowels:
                current_vowels.append(letter)
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = current_vowels.pop(-1)
        return "".join(s_list)