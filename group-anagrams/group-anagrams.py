class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        result = {}
        for word in words:
            sorted_word = "".join(sorted(word))
            if sorted_word not in result.keys():
                result[sorted_word] = [word]
            else:
                result[sorted_word].append(word)
        return result.values()