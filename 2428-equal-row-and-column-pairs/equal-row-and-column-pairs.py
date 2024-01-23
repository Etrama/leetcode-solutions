class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # grid itself is a list of rows
        # make a list of columns
        columns = []
        for i in range(len(grid)):
            column = []
            for row in grid:
                column.append(row[i])
            columns.append(column)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i] == columns[j]:
                    count += 1
        return count