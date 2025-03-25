from abc import ABC, abstractmethod

class InterfaceItensServico(ABC):
    @abstractmethod
    def informacaoServiço(self):
        pass

    @abstractmethod
    def getValorTotal(self):
        pass