'''Crie um programa que implemente uma função que, dada uma lista, retorne a moda
da lista, ou seja, uma lista com o(s) elemento(s) mais frequente(s) da lista original.'''

def encontrar_moda(lista):
    if not lista:
        return []  #teste de erro, para não receber lista vazia
    
    moda = []
    maiorFrequencia = 0

    for elemento in lista:
        frequencia = 0
        for item in lista:
            if item == elemento: 
                frequencia += 1

#contador para ver quantas vezes o item aparece na lista

        if frequencia > maiorFrequencia:
            maiorFrequencia = frequencia 
            moda = [elemento]
        elif frequencia == maiorFrequencia and elemento not in moda:
            moda.append(elemento)

    return moda

quantidade_elementos = int(input("Digite quantos elementos você deseja em sua lista: "))

lista = []
for i in range(quantidade_elementos):
    numero = int(input(f"Digite o número {i+1}: "))
    lista.append(numero)

resultado = encontrar_moda(lista)
print("A moda dessa lista é: ", resultado)





