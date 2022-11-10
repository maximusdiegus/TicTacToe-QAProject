from enum import Enum

class GameStatus(Enum):
    InProgress = 1
    Draw = 2
    FirstPlayerWin = 3
    SecondPlayerWin = 4