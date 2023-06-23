class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ref_dict = dict(zip(alphabets, morse_code))
        encoded = []
        for word in words:
            result = ""
            for letter in word:
                result += ref_dict[letter]
            encoded.append(result)
        return len(set(encoded))