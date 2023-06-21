class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabets ="abcdefghijklmnopqrstuvwxyz "
        key = key.replace(" ", "")
        key += " "
        # print(key)
        ref_dict = {}
        alpha_index = 0
        for letter in key:
            if ref_dict.get(letter, 0) == 0:
                ref_dict[letter] = alphabets[alpha_index]
                alpha_index += 1
        # print(ref_dict)
        result = [ref_dict[i] for i in message]
        return "".join(result)