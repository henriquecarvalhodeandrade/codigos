from typing import Type
from maoObra import MaoObra
from produto import Produto

class Servico():
    def __init__(self, produto: Type[Produto], maoObra: Type[MaoObra]):
        self.__produto = produto
        self.__maoObra = maoObra

    def calcularValorServico(self):
        return self.__maoObra.getValorTotal() + self.__produto.getValorTotal()
    
    def mostrarServico(self):
        return (f"Produto: {self.__produto.getTipo()}, Valor Total: {self.__produto.getValorTotal()}\n"
                f"Mão de Obra: {self.__maoObra.getDescricao()}, Valor: {self.__maoObra.getValorTotal()}")