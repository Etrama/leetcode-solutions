class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        if ruleKey == "type":
            for x, _, _ in items:
                if x == ruleValue:
                    count += 1
        elif ruleKey == "color":
            for _, y, _ in items:
                if y == ruleValue:
                    count += 1
        elif ruleKey == "name":
            for _, _, z in items:
                if z == ruleValue:
                    count += 1
        return count

        
             