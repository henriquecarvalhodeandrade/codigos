
# Aluno: Henrique Carvalho de Andrade
# Matrícula: JC3033732
# Exercício escolhido: 08

# Enunciado:
'''
Caros alunos,

Fazer os exercícios 8 ou 9 do arquivo da aula, em anexo.

O aluno deve desenvolver a solução dos problemas, utilizando linguagem Python ou C++.

Ver as orientações no documento, observando quais são as variáveis de entrada e de saída obrigatórias.

Fazer um vídeo explicando o algoritmo criado, executando os testes, com 3 acertos e 3 erros. Duração de, no máximo, 10 minutos.

Enviar somente o link do vídeo e o arquivo do código para que eu possa testá-lo.

Enviar um arquivo contendo a descrição matemática completa da resolução do problema. Orientar-se pela resolução feita na sala de aula, observando que não podem ser substituídos por valores, mas sim por variáveis.

Abraços,

Aline
'''

# Questão: Minimizar o custo de um material cilíndrico.
# Entradas: Volume, com ou sem tampa, custos das bases. (fornecidas pelo usuário)
# Saídas: Dimensões, custo das bases e custo total.
# OBS: 1 ml = 1 cm³

# --------------------------------------------------------------------------------------------
# volume = base . altura
# volume = (pi . r²) . h

# h = volume / (pi . r²)

# area base = pi . r²
# area lateral = 2 . pi . r . h

# area total =              area lateral              +   area base   . quantidade de bases 
# area total =            (2 . pi . r . h)            +   (pi . r²)   . quntidade bases
# area total =  {2 . pi . r . [volume / (pi . r²)]}   +   (pi . r²)   . quntidade bases

# derivar a area e igualar a zero
# encontrar o raio
# encontrar a altura
# assim, chegaremos nas medidas que reduzem o preço o máximo possível.
# --------------------------------------------------------------------------------------------
import math




class Cilindro:
    def __init__(self, volume, valor_base, valor_lateral, com_tampa):
        if volume <= 0:
            raise ValueError("O volume deve ser um valor positivo.")
        if valor_base < 0 or valor_lateral < 0:
            raise ValueError("Os valores da base e da lateral devem ser não negativos.")
        if com_tampa not in [0, 1]:
            raise ValueError("O valor para tampa deve ser 0 (sem tampa) ou 1 (com tampa).")
        
        self.volume = volume
        self.valor_base = valor_base
        self.valor_lateral = valor_lateral
        self.com_tampa = com_tampa
        self.raio = None
        self.altura = None
        self.custo_base = None
        self.custo_lateral = None
        self.custo_total = None

    def calcular_dimensoes(self):
        # Calcular o raio que minimiza a área total
        if self.com_tampa:
            self.raio = (self.volume / (2 * math.pi))**(1/3)
        else:
            self.raio = (self.volume / (math.pi))**(1/3)

        self.altura = self.volume / (math.pi * self.raio**2)

    def calcular_custo(self):
        area_base = math.pi * self.raio**2
        area_lateral = 2 * math.pi * self.raio * self.altura
        self.custo_base = area_base * self.valor_base
        self.custo_lateral = area_lateral * self.valor_lateral

        if self.com_tampa:
            self.custo_total = 2 * self.custo_base + self.custo_lateral
        else:
            self.custo_total = self.custo_base + self.custo_lateral

    def mostrar_resultados(self):
        print(f"\nRaio: {self.raio:.2f} cm")
        print(f"Altura: {self.altura:.2f} cm")
        print(f"Custo total das bases: R$ {self.custo_base:.2f}")
        print(f"Custo total da lateral: R$ {self.custo_lateral:.2f}")
        print(f"Custo total do cilindro: R$ {self.custo_total:.2f}")




def main():
    try:
        print("\nEste programa fará:\n - calcula as dimensões e o custo total de um cilindro com base no volume fornecido pelo usuário\n - usuário pode especificar se o cilindro possui uma tampa ou não\n - o programa determina o raio e a altura que minimizam o custo total do cilindro\n - exibe as dimensões (raio e altura) e o custo total\n - OBS: 1 ml = 1cm³")

        volume = float(input("\nVolume (ml)\n: "))
        valor_base = float(input("\nValor da base (R$/cm²)\n: "))
        valor_lateral = float(input("\nValor da lateral (R$/cm²)\n: "))
        tampa = int(input("\nDigite:\n[1] - com tampa // [0] - sem tampa\n: "))

        cilindro = Cilindro(volume, valor_base, valor_lateral, tampa)
        cilindro.calcular_dimensoes()
        cilindro.calcular_custo()

        print("\nResultados:")
        cilindro.mostrar_resultados()
        print()

    except ValueError as e:
        print(f"\nErro: {e}")



main()




