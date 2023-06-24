class Solution:
    def countAsterisks(self, s: str) -> int:
        star_count = 0
        bar_count = 0
        for letter in s:
            if letter == "|":
                bar_count += 1
            if bar_count % 2 == 0 and letter == "*":
                star_count += 1
        return star_count