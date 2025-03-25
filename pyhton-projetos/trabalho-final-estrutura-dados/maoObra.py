from interfaceItensServico import InterfaceItensServico

class MaoObra(InterfaceItensServico):
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor  

    def informacaoServiço(self):
        return f"Servçio prestado\n{self.__descricao}\n\nValor total\n{self.__valor}"

    def getValorTotal(self):
        return self.__valor  
    
    def getDescricao(self):
        return self.__descricao

    def setDescricao(self, descricao):
        self.__descricao = descricao


    def setValor(self, valor):
        self.__valor = valor