'''Implemente um programa com uma função que, dada uma lista, retorne outra lista,
com os elementos da lista original, sem repetições.'''

n = int(input("Digite quantos elementos você quer na sua lista: "))
lista_original = []

for i in range(n):
    elementos_lista = (input("Escreva os elementos de sua lista: "))
    lista_original.append(elementos_lista)
    

def removerRepeticao(lista):
    lista_sem_repetidos = []
    for elemento in lista:
        if elemento not in lista_sem_repetidos:
            lista_sem_repetidos.append(elemento)
    return lista_sem_repetidos

lista_sem_repetidos = removerRepeticao(lista_original)
print(lista_sem_repetidos)
