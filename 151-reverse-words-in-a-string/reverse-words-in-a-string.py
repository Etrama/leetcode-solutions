class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split(" ")
        words_new = []
        for word in words:
            if word != "":
                words_new.append(word)
        return " ".join(words_new[::-1])