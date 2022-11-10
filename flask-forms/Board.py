from array import *
from Enum.Symbol import Symbol

class Board:
   
    def __init__(self, dimX, dimY):
        self.dimX = dimX
        self.dimY = dimY
        self.board = [[Symbol.Dot.value for i in range(self.dimX)] for i in range(self.dimY)]
    
    def putSymbol(self, posX, posY, symbol):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if posX == i and posY == j:
                    self.board[i][j] = symbol
                    
        if self.checkWin(symbol):
            print("Yeah")
        else:
            print("Nah")
        
                
    def checkWin(self, symbol):
        match = True
        
        '''Check Row'''
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != symbol:
                    match = False
            if match == True:
                return True
            else:
                match = True
            
        if match == False:
            match = True
                          
        '''Check Column'''
        columnArray = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                columnArray.append(self.board[j][i])
                match = all(ele == symbol for ele in columnArray)
                
            if match == True:
                return True
            else:
                match = True    
        
        if match == False:
            match = True
        
        '''Check Diagonal'''
        diagonalArray = []
        for i in range(len(self.board)):
            diagonalArray.append(self.board[i][i])
            match = all(ele == symbol for ele in diagonalArray)
            if match == True:
                return True
            else:
                match = True
        
        '''Check Diagonal Backwards'''
        j = 0
        k = len(self.board) -1
        diagonalArray = []
        
        for i in range(len(self.board)):
            diagonalArray.append(self.board[j][k])
            j += 1
            k -= 1
        match = all(ele == symbol for ele in diagonalArray)
        
        if match:
            return True
        else:
            return False
            
    
    def printBoard(self):
        for i in range(len(self.board)):
            print("| ", end="")
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=" ")
            print("|")
            
foo = Board(3,3)
foo.printBoard()
foo.putSymbol(0,2,Symbol.Cross.value)
foo.putSymbol(1,1,Symbol.Cross.value)
foo.putSymbol(2,0,Symbol.Cross.value)
foo.printBoard()
