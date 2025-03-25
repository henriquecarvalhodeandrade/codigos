class Cliente:
    def __init__(self, nome, telefone, seguradora, localidade):
        self.__nome = nome
        self.__telefone = telefone
        self.__seguradora = seguradora
        self.__localidade = localidade

    def getLocal(self):
        return self.__localidade
    
    def setLocal(self, localidade):
        self.__localidade = localidade

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getTelefone(self):
        return self.__telefone

    def setTelefone(self, telefone):
        self.__telefone = telefone

    def getSeguradora(self):
        return self.__seguradora

    def setSeguradora(self, seguradora):
        self.__seguradora = seguradora

    def __str__(self):
        return (f"Nome: {self.__nome}\n"
                f"Telefone: {self.__telefone}\n"
                f"Seguradora: {self.__seguradora}\n"
                f"Local: {self.__localidade}")