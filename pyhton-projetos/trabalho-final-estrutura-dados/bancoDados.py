from linkedList import *
from binarySearchTree import *
from graph import *

class BancoDeDados:
    contagem_itens = {
        'itens': 0,
        'funcionarios': 0,
        'orcamentos': 0
    }

    def __init__(self):
        self.itens = linked_list()
        self.funcionarios = BinarySearchTree()
        self.localizações = Graph("São José dos Campos")
        self.orcamentos = {}

    def exibir_contagem(self):
        return BancoDeDados.contagem_itens