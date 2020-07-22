class Solution:
    def EmptyLoc(self,board, l1):
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    l1[0]=i
                    l1[1]=j
                    return True
        return False
    def isRow(self,board, row, num):
        for i in range(9):
            if board[row][i]==str(num):
                return False
        return True
    def isCol(self,board, col, num):
        for i in range(9):
            if board[i][col]==str(num):
                return False
        return True
    def isGrid(self,board, row, col, num):
        for i in range(3*row,3*(row+1)):
            for j in range(3*col,3*(col+1)):
                if board[i][j]==str(num):
                    return False
        return True
    def isSafe(self,board, row, col, num):
        return self.isRow(board, row, num) and self.isCol(board, col, num) and self.isGrid(board, row//3, col//3, num)
    def solve(self, board):
        l=[-1,-1]
        if not self.EmptyLoc(board,l):
            return True
        for i in range(1,10):
            if self.isSafe(board, l[0], l[1], i):
                board[l[0]][l[1]]=str(i)
                if self.solve(board):
                    return True
                board[l[0]][l[1]]="."
        return False
        
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        return board


obj=Solution()
board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board=[[".","5",".",".","1",".",".",".","6"],["3",".",".","5",".","8",".","9","."],[".",".",".",".",".","7",".","4","."],[".",".",".",".",".",".",".","2","."],[".","9",".",".",".","3","1",".","."],[".",".",".",".",".","1",".",".","9"],[".","8",".","3","6",".","9",".","5"],["9","2",".",".",".",".",".",".","."],["6",".",".",".","7",".",".","8","."]]
board=obj.solveSudoku(board)
for row in range(9):
	for col in range(9):
		print(board[row][col],end=" ")
	print()