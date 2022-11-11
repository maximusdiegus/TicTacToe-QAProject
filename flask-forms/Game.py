from Enum.GameStatus import GameStatus
from Enum.Symbol import Symbol
from Board import Board


class Game:
    
    board: Board
    
    def __init__ (self, board, firstPlayer, secondPlayer, playerTurn, move, gameStatus):
        self.board = board