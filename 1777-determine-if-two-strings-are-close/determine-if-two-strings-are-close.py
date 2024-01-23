class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        sword1, sword2 = sorted(word1), sorted(word2)
        if sword1 == sword2:
            return True
        else:
            count_dict1, count_dict2 = {}, {}
            for char in sword1:
                if char not in count_dict1:
                    count_dict1[char] = sword1.count(char)
            for char in sword2:
                if char not in count_dict2:
                    count_dict2[char] = sword2.count(char)
            count1 = sorted(list(count_dict1.values()))
            count2 = sorted(list(count_dict2.values()))
            condition1 = count_dict1.keys() == count_dict2.keys()
            condition2 = count1 == count2
            return condition1 and condition2