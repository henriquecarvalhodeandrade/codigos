'''Crie um programa que implemente e teste uma função para cada item abaixo, dadas
duas listas representando dois conjuntos, que:
a. Retorne uma lista que represente a união dos dois conjuntos.
b. Retorne uma lista que represente a interseção dos dois conjuntos.
c. Retorne uma lista que represente a diferença entre os dois conjuntos.
d. Verifique se o primeiro é um subconjunto do segundo.'''

def uniao(conjunto1,conjunto2):
    resultado = []
    for elemento in conjunto1:
        if elemento not in resultado:
            resultado.append(elemento)
    for elemento in conjunto2:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

def intersecao(conjunto1,conjunto2):
    resultado = []
    for elemento in conjunto1:
        if elemento in conjunto2 and elemento not in resultado:
            resultado.append(elemento)
    return resultado

def diferenca(conjunto1,conjunto2):
    resultado = []
    for elemento in conjunto1:
        if elemento not in conjunto2 and elemento not in resultado:
            resultado.append(elemento)
    return resultado

def subconjunto(conjunto1,conjunto2):
    for elemento in conjunto1:
        if elemento not in conjunto2:
            return False
    return True

quantidade_elemento1 = int(input("Digite quantos elementos você deseja no conjunto 1: "))

conjunto1 = [] 
for i in range(quantidade_elemento1):
    elemento = input(f"Digite o número {i+1}: ")
    conjunto1.append(elemento)

quantidade_elemento2 = int(input("Digite quantos elementos você deseja no conjunto 2: "))

conjunto2 = []
for i in range(quantidade_elemento2):
    elemento = input(f"Digite o número {i+1}: ")
    conjunto2.append(elemento)

print()
print("Conjunto 1: ", conjunto1)
print("Conjunto 2: ", conjunto2)

#resultado

print()
print("A união é: ", uniao(conjunto1,conjunto2))
print("A interseção é: ", intersecao(conjunto1,conjunto2))
print("A diferença do conjunto 1 - conjunto 2: ", diferenca(conjunto1,conjunto2))
print("O conjunto 1 é subconjunto do 2: ", subconjunto(conjunto1,conjunto2))
print()








