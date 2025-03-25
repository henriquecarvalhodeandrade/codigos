from item import *

class ValidadorTinta:
    @staticmethod
    def validar_nome(nome):
        if not isinstance(nome, str):
            raise ValueError("O nome deve ser uma string.")

    @staticmethod
    def validar_codigo(codigo):
        if not isinstance(codigo, str):
            raise ValueError("O código deve ser uma string.")

    @staticmethod
    def validar_quantidade(quantidade):
        if not isinstance(quantidade, int) or quantidade < 0:
            raise ValueError("A quantidade deve ser um número inteiro não negativo.")

    @staticmethod
    def validar_cor(cor):
        if not isinstance(cor, str):
            raise ValueError("A cor deve ser uma string.")

    @staticmethod
    def validar_volume(volume):
        if not isinstance(volume, (int, float)) or volume <= 0:
            raise ValueError("O volume deve ser um número positivo.")

class Tinta(Item):
    def __init__(self, nome: str, codigo: str, quantidade: int, cor: str, volume: float):
        super().__init__(nome, codigo, quantidade)
        self.cor = cor
        self.volume = volume

    def get_detalhes(self):
        return f"Cor: {self.cor}, Volume: {self.volume}ml"

    def get_cor(self):
        return self.cor

    def set_cor(self, valor):
        ValidadorTinta.validar_cor(valor)
        self.cor = valor

    def get_volume(self):
        return self.volume

    def set_volume(self, valor):
        ValidadorTinta.validar_volume(valor)
        self.volume = valor

    def __str__(self):
        return f"nome: {self.nome}, codigo: {self.codigo}, quantidade: {self.quantidade}, cor: {self.cor}, volume: {self.volume}ml"