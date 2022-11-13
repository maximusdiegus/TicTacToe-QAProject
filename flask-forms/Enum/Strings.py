from enum import Enum

class Strings(Enum):
    Menu = "Menu: "
    MenuStartGame = "Start new game."
    MenuLoadGame = "Load game."
    MenuExitGame = "Exit game."
    ErrorPutSymbol = "Invalid movement. You cannot put a tile in that position."
    FirstPlayerWins = "Congrats! 1st player wins."
    SecondPlayerWins = "Congrats! 2nd player wins."
    
    ExceptionFileNotSaved = "File could not be saved! :( This is the error: "
    ExceptionFileNotLoaded = "File could not be loaded! :( This is the error: "
    