'''Escreva uma função que dada uma matriz quadrada, verifique se ela é uma matriz
diagonal.'''

n = int(input("Digite a ordem da matriz quadrada (n x n): "))
matriz = []

print("Dgite os elementos da matriz,um por vez: ")

for i in range(n):
    linha = []
    for j in range(n):
        coluna = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(coluna)
    matriz.append(linha)

print(matriz)
print()

diagonal = True
for i in range(n):
    for j in range(n):
        if i != j and matriz[i][j] != 0:
            diagonal = False
            break
    if not diagonal:
        break        #esta percorrendo todas as linhas da matriz, para testar se é diagonal

if diagonal:
    print("A matriz é diagonal.")
else:
    print("A matriz não é diagonal.")
