class Solution:
    def sortVowels(self, s: str) -> str:
        # alphabets = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        vowels = set("AEIOUaeiou")
        # consonants = set(alphabets) - vowels
        vowel_array = []
        t = []
        for i in s:
            if i in vowels:
                vowel_array.append(i)
        vowel_array = sorted(vowel_array, key=lambda x: ord(x))
        for i in range(len(s)):
            if s[i] in vowels:
                t.append(vowel_array.pop(0))
            else:
                t.append(s[i])
        return "".join(t)

