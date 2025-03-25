from item import *

class ValidadorPeca:
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
    def validar_especificacao(especificacao):
        if not isinstance(especificacao, str):
            raise ValueError("A especificação deve ser uma string.")

class Peca(Item):
    def __init__(self, nome: str, codigo: str, quantidade: int, especificacao: str):
        super().__init__(nome, codigo, quantidade)
        self.especificacao = especificacao

    def get_detalhes(self):
            return f"Especificação: {self.especificacao}"

    def set_especificacao(self, valor):
        ValidadorPeca.validar_especificacao(valor)
        self._especificacao = valor

    def __str__(self):
        return f"nome: {self.nome}, codigo: {self.codigo}, quantidade: {self.quantidade}, especificacao: {self.especificacao}"