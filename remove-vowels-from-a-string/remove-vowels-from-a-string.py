class Solution:
    def removeVowels(self, s: str) -> str:
        result = []
        vowels = {"a":"","e":"","i":"","o":"","u":"",}
        for char in s:
            if vowels.get(char) is None:
                result.append(char)
        return "".join(result)
