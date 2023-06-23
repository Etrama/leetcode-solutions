class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        ref_dict = {alpha:0 for alpha in alphabets}
        for letter in sentence:
            ref_dict[letter] += 1
        for count in ref_dict.values():
            if count == 0:
                return False
        return True