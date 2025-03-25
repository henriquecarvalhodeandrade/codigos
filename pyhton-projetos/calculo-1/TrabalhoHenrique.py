import numpy as np

# Função para calcular os valores da função trigonométrica
def calculate_function(A, b, c, d, func_type):
    x_values = np.linspace(-2 * np.pi, 2 * np.pi, 20)  # Gera 20 valores de x
    results = []

    for x in x_values:
        if func_type == 'sen':
            y = A * np.sin(b * x + c) + d
        elif func_type == 'cos':
            y = A * np.cos(b * x + c) + d
        else:
            raise ValueError("Tipo de função inválido. Use 'sen' ou 'cos'.")
        
        results.append((x, y))
    
    return results

# Função para exibir os resultados
def display_results(results):
    print("x\t\tf(x)")
    print("------------------------")
    for x, y in results:
        print(f"{x:.2f}\t{y:.2f}")

# Entrada do usuário
A = float(input("Digite o valor de A (amplitude): "))
b = float(input("Digite o valor de b (frequência): "))
c = float(input("Digite o valor de c (deslocamento horizontal): "))
d = float(input("Digite o valor de d (deslocamento vertical): "))
func_type = input("Digite o tipo de função (sen ou cos): ")

# Cálculo dos valores da função
results = calculate_function(A, b, c, d, func_type)

# Exibição dos resultados
display_results(results)


'''

1. Importação de Biblioteca:
    numpy é utilizado apenas para gerar os valores de x.


2. Função calculate_function:
    Gera 20 valores de x entre -2π e 2π.
    Calcula os valores de y com base na função trigonométrica escolhida (seno ou cosseno).
    Armazena os pares de valores (x, y) em uma lista.


3. Função display_results:
    Imprime os valores de x e f(x) em formato de tabela.


4. Entrada do Usuário:
    O usuário insere os valores de A, b, c, d e o tipo de função.
    Cálculo e Exibição:

    A função calculate_function é chamada para calcular os valores, e display_results exibe os resultados.

'''
