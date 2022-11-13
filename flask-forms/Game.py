from Enum.GameStatus import GameStatus
from Enum.Symbol import Symbol
from Enum.Strings import Strings
from Board import Board
from IPlayer import IPlayer
import json


class Game:
        
    def __init__ (self):
        self.board = Board(3,3)
        self.firstPlayer = IPlayer()
        self.secondPlayer = IPlayer()
        self.playerTurn = 1
        '''self.move = move'''
        self.gameStatus = GameStatus.Start.value
        self.gameName = ""
        
    def menu():
        print("----------------")
        print("| " + Strings.Menu + " |")
        print("| " + Strings.MenuStartGame + " |")
        print("| " + Strings.MenuLoadGame + " |")
        print("| " + Strings.MenuExitGame + " |")
        print("----------------")
        
    def play(self, dimX, dimY, player):
        symbol = player.symbol
        notErrorMove = False
        
        if self.gameStatus == GameStatus.Start.value:
            self.setGameStatus(GameStatus.InProgress.value)
        
        while notErrorMove == False:
            notErrorMove = self.board.putSymbol(dimX, dimY, symbol)
            if notErrorMove == False:
                Strings.ErrorPutSymbol.value
        
        self.printCurrentBoard()
        self.gameStatus = self.board.checkWin(symbol)
        self.setPlayerTurn(2)
        
        if self.getGameStatus == True:
            self.showWinMessage(player)
        else:
            self.setGameStatus

    def printCurrentBoard(self):
        self.board.printBoard()
    
    def setGameStatus(self, gameStatus):
        self.gameStatus = gameStatus
    
    def getGameStatus(self):
        return (self.gameStatus)
    
    def showWinMessage(self, player):
        if player.getFirstOrSecondPlayer() == 1:
            print(Strings.FirstPlayerWins.value)
        else:
            print(Strings.SecondPlayerWins.value)
    
    def setPlayerTurn(self, playerTurn):
        self.playerTurn = playerTurn
    
    def getPlayerTurn(self):
        return (self.playerTurn)
    
    def saveGame(self, name):
        
        try:
            
            file = open(name + ".json", "w")
            
            infoToSave = {
                "gameName": name,
                "Player1": self.firstPlayer.getName(),
                "Player2": self.secondPlayer.getName(),
                "BoardStatus": self.board.board,
                "GameStatus": self.getGameStatus(),
                "Turn": self.getPlayerTurn()
            }
            
            json.dump(infoToSave, file, indent = 1)
            file.close()
            
        except Exception as e:
            print(Strings.ExceptionFileNotSaved)
            print(e)
    
        
    def loadGame(self, name):
        try:
            file = open(name + '.json')
            data = json.loads(file)
            
            self.game = data["gameName"]
            self.firstPlayer.name = data["Player1"]
            self.secondPlayer.name = data["player2"]
            self.board = data["BoardStatus"]
            self.setGameStatus(data["GameStatus"]) 
            self.setPlayerTurn(data["BoardStatus"]) 
            
        except Exception as e:
            print(Strings.ExceptionFileNotLoaded)
            print(e)
        