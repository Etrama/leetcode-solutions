class Solution:
    def romanToInt(self, s: str) -> int:
        mapping_double = {
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900
        }
        mapping_single = { "I" : 1,
                    "V" : 5,
                    "X" : 10,
                    "L" : 50,
                    "C" : 100,
                    "D" : 500,
                    "M" : 1000}
        index = 0
        value = 0
        while index < len(s):
            # print(index)
            if (index < len(s) - 1)and (s[index] + s[index+1] in mapping_double):
                # print("Double")
                value += mapping_double[s[index] + s[index+1]]
                index += 2
                continue
            if s[index] in mapping_single:
                # print("Single")
                value += mapping_single[s[index]]
                index += 1
        return value