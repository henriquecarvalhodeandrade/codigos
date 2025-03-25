class Veiculo:
    def __init__(self, nome, quilometragem, montadora, placa, ano, chassi, frota):
        self.__nome = nome
        self.__quilometragem = quilometragem
        self.__montadora = montadora
        self.__placa = placa
        self.__ano = ano
        self.__chassi = chassi
        self.__frota = frota

  
    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getQuilometragem(self):
        return self.__quilometragem

    def setQuilometragem(self, quilometragem):
        self.__quilometragem = quilometragem

    def getMontadora(self):
        return self.__montadora

    def setMontadora(self, montadora):
        self.__montadora = montadora

    def getPlaca(self):
        return self.__placa

    def setPlaca(self, placa):
        self.__placa = placa

    def getAno(self):
        return self.__ano

    def setAno(self, ano):
        self.__ano = ano

    def getChassi(self):
        return self.__chassi

    def setChassi(self, chassi):
        self.__chassi = chassi

    def getFrota(self):
        return self.__frota

    def setFrota(self, frota):
        self.__frota = frota

    
    def __str__(self):
        return (f"Veículo: {self.__nome}\n"
                f"Quilometragem: {self.__quilometragem} km\n"
                f"Montadora: {self.__montadora}\n"
                f"Placa: {self.__placa}\n"
                f"Ano: {self.__ano}\n"
                f"Chassi: {self.__chassi}\n"
                f"Frota: {self.__frota}")