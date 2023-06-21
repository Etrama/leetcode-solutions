class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cells = s.split(":")
        row1 = int(cells[0][-1])
        row2 = int(cells[1][-1])
        # print(row1, row2)
        letter1 = cells[0][0]
        letter2 = cells[1][0]
        letter1 = alphabets.index(letter1)
        letter2 = alphabets.index(letter2)
        result = []
        for i in range(letter1, letter2+1):
            for j in range(row1, row2+1):
                result.append(alphabets[i]+str(j))
        # print(result)
        return result