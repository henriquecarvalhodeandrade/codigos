class Funcionario:
    def __init__(self, nome: str, cpf: str, salario: float, cargo: str, id: int):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo
        self.id = id
        
    def __str__(self):
        return f"nome: {self.nome}, cpf: {self.cpf}, salario: R${self.salario}, cargo: {self.cargo}, id: {self.id}"
