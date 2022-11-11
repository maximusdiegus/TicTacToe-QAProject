from abc import abstractmethod

class IPlayer:
    
    @abstractmethod
    def getSymbol(self):
        pass
    
    @abstractmethod
    def getName(self):
        pass