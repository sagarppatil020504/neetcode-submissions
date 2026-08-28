from typing import List
class Solution:
   
    def box(self,board:List[List[str]], x_dir,y_dir)-> bool:
        
        section=[]
 
        for x in range(x_dir,x_dir+3):
            for y in range(y_dir,y_dir+3):
                # This checks if the number is repeated
                if board[x][y]==".":
                    continue
                if board[x][y] in section: 
                    return False
                else:
                    section.append(board[x][y])
        return True
    
    def straight(self, board, pos):
        section = []

        for i in range(len(board)):
            if board[pos][i]==".":
                continue
            if board[pos][i] in section:
                return False
            else:
                section.append(board[pos][i])

        section.clear()
        
        for i in range(len(board)):
            if board[i][pos]==".":
                continue
            if board[i][pos] in section:
                return False
            else:
                section.append(board[i][pos])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            if not self.straight(board, i):
                return False

        for x in range(0,9,3):        
            for y in range(0,9,3):

                if not self.box(board,x,y):
                    return False
        return True