'''
10. Usando algoritmos recursivos, escreva funções que:
a. Defina uma função que recebe como argumento uma lista de inteiros e devolva
o produto dos seus elementos.
b. Defina uma função que recebe como argumento uma lista de números inteiros
w e devolve True se w contém um número par e False em caso contrário.
c. Defina uma função que recebe como argumento uma lista de números inteiros
w e devolve True se w contém apenas números ímpares e False em caso
contrário.
'''
NEGRITO = "\033[1m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CIANO = "\033[36m"
BRANCO = "\033[37m"
RESET = "\033[0m"

print(VERDE + "-" *100)
print('''
  _____           _           _             _                _____           _     _           _      
 |  __ \         | |         | |           (_)              |  __ \         (_)   | |         | |     
 | |__) | __ ___ | |__   __ _| |_ ___  _ __ _  ___     ___  | |__) |_ _ _ __ _  __| | __ _  __| | ___ 
 |  ___/ '__/ _ \| '_ \ / _` | __/ _ \| '__| |/ _ \   / _ \ |  ___/ _` | '__| |/ _` |/ _` |/ _` |/ _ |
 | |   | | | (_) | |_) | (_| | |_ (_) | |  | | (_) | |  __/ | |  | (_| | |  | | (_| | (_| | (_| |  __/
 |_|   |_|  \___/|_.__/ \__,_|\__\___/|_|  |_|\___/   \___| |_|   \__,_|_|  |_|\__,_|\__,_|\__,_|\___|
                                                                                                      
                                                                                                      
''')
print( "-" *100 + RESET)
print()

def probatorio(lista,acumulador,indice):
    if indice < len(lista):
        acumulador *= lista[indice]
        return probatorio(lista,acumulador, indice + 1)
    else:
        return acumulador
    
def numero_par(w,indice):
    if indice >= len(w):
        return False
    if w[indice] % 2 == 0:
        return True
    else: 
        return numero_par (w,indice + 1)

def numero_impar(w,indice):
    if indice >= len(w):
        return True
    if w[indice] % 2 == 0:
        return False
    else:   
        return numero_impar (w,indice + 1)
    
lista_inteiros=[]
elementos_limite = -1

while elementos_limite <= 0:
    elementos_limite = int(input(AZUL + "Digite a quantidade de elementos a serem multiplicados: "+ RESET))
    if elementos_limite <= 0:
        print(VERMELHO + "Digite um valor válido!!!" + RESET)

print(AZUL + "Digite os elemento para ser multiplicados: " + RESET)
for i in range(elementos_limite):
    elemento=int(input(AMARELO + ">> " + RESET))
    lista_inteiros.append(elemento)

print(f"{MAGENTA}{NEGRITO}O produtório desses números: {RESET} ")
print(f' {AMARELO}{probatorio(lista_inteiros,1,0)}{RESET}')
print()

paridade_lista = numero_par(lista_inteiros,0)
paridade_lista_impar = numero_impar(lista_inteiros,0)

if paridade_lista == True or paridade_lista_impar == False :
    print(f'{AMARELO}A lista possui números pares{RESET}')
else:
    print(f'{AMARELO}A lista não possui números pares')
