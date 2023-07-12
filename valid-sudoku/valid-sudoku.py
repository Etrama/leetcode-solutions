import collections
class Solution:
    def validRows(self, board):
        for row in board:
            count_dict = collections.Counter(row)
            for key, value in count_dict.items():
                if key != "." and value > 1:
                    return False
        return True

    def validColumns(self, board):
        for i in range(0,9):#all columns
            temp = []
            for j in range(0,9):
                temp.append(board[j][i])
            count_dict = collections.Counter(temp)
            for key, value in count_dict.items():
                if key != "." and value > 1:
                    return False
        return True

    def validSquare(self, board):
        middle_squares = [(1,1), (1,4), (1,7),
                           (4,1), (4,4), (4,7),
                           (7,1), (7,4), (7,7),]
        for square in middle_squares:
            temp = []
            temp.append(board[square[0]][square[1]]) #middle
            temp.append(board[square[0]-1][square[1]-1]) #top left
            temp.append(board[square[0]+1][square[1]+1]) #bottom right
            temp.append(board[square[0]][square[1]-1])
            temp.append(board[square[0]][square[1]+1])
            temp.append(board[square[0]-1][square[1]])
            temp.append(board[square[0]+1][square[1]])
            temp.append(board[square[0]+1][square[1]-1])
            temp.append(board[square[0]-1][square[1]+1])
            count_dict = collections.Counter(temp)
            for key, value in count_dict.items():
                if key != "." and value > 1:
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = self.validRows(board)
        # print(row_check)
        col_check = self.validColumns(board)
        # print(col_check)
        square_check = self.validSquare(board)
        # print(square_check)
        return row_check and col_check and square_check