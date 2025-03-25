class Passaro():
    def __init__(self, nome, raca, tamanho):
        self.nome = nome
        self.raca = raca
        self.tamanho = tamanho

    def cantar(self):
        return print(f'\nO passarinho {self.nome} está cantando.')

    def alimentarSe(self):
        return print(f'\n{self.nome} está se alimentando no momento.')
    
    def dormir(self):
        return print(f'\n{self.nome} vai tirar um cochilo...')
    
    def informacoes(self):
        return print(f'\nO passáro é um {self.raca}, seu nome é {self.nome} e possui tamanho de {self.tamanho}cm.')



