class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        index = -1
        for word in sentence:
            if searchWord == word[:len(searchWord)]:
                index = sentence.index(word) + 1
                break
        return index