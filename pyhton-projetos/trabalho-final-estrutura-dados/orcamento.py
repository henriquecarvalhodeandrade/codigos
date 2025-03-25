from veiculo import Veiculo
from servico import Servico
from cliente import Cliente
from datetime import date
from typing import Type

class Orcamento:
    def __init__(self, codigo, data_entrada: date, veiculo: Veiculo, servico: Servico, cliente: Cliente):
        self.__codigo = codigo
        self.__data_entrada = data_entrada
        self.__veiculo = veiculo
        self.__servico = servico
        self.__cliente = cliente

    def juntarInfo(self):
        # Organizando as informações em um formato mais legível e bonito
        veiculo_info = (
            f"Nome: {self.__veiculo.getNome()}\n"
            f"Quilometragem: {self.__veiculo.getQuilometragem()} km\n"
            f"Montadora: {self.__veiculo.getMontadora()}\n"
            f"Placa: {self.__veiculo.getPlaca()}\n"
            f"Ano: {self.__veiculo.getAno()}\n"
            f"Chassi: {self.__veiculo.getChassi()}\n"
            f"Frota: {self.__veiculo.getFrota()}\n"
        )

        cliente_info = (
            f"Nome: {self.__cliente.getNome()}\n"
            f"Telefone: {self.__cliente.getTelefone()}\n"
            f"Seguradora: {self.__cliente.getSeguradora()}\n"
        )

        servico_info = f"Serviço: {self.__servico.mostrarServico()}\n"
        
        # Retornando todas as informações de forma organizada
        return (
            f"===== ORÇAMENTO =====\n"
            f"Código: {self.__codigo}\n"
            f"Data de Entrada: {self.__data_entrada}\n\n"
            f"--- VEÍCULO ---\n"
            f"{veiculo_info}\n"
            f"--- SERVIÇO ---\n"
            f"{servico_info}\n"
            f"--- CLIENTE ---\n"
            f"{cliente_info}\n"
            "====================="
        )

    def getCodigo(self):
        return self.__codigo

    def definirCodigo(self, codigo):
        self.__codigo = codigo

    def getData(self):
        return self.__data_entrada

    def setData(self, data_entrada):
        self.__data_entrada = data_entrada

    def getVeiculo(self): # Getter for veiculo
        return self.__veiculo

    def getServico(self):  # Getter for servico
        return self.__servico

    def getCliente(self):  # Getter for cliente
        return self.__cliente

    def setVeiculo(self, veiculo): # Setter for veiculo (for completeness)
        self.__veiculo = veiculo

    def setServico(self, servico): # Setter for servico (for completeness)
        self.__servico = servico

    def setCliente(self, cliente): # Setter for cliente (for completeness)
        self.__cliente = cliente