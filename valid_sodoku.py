class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))
    


    def isValidSudoku2(self, board):
        #check rows
        for i in range(9):
            if not self.checkList(board[i]):
                return False
            
        #check columns
        for j in range(9):
            column = [board[i][j] for i in range(9)]
            if not self.checkList(column):
                return False
            
        #check 3x3
        for i in range(0,9,3):
            for j in range(0,9,3):
               subgrid = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
               if not self.checkList(subgrid):
                   return False
        
        return True 

    def checkList(self, nums):
        x = set()
        for i in nums:
            if i != '.':
                if i in x:
                    return False
                x.add(i)
        return True






s = Solution()
print(s.isValidSudoku2(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))