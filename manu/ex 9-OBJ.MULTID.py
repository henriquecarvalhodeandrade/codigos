'''Escreva uma função que dada uma matriz quadrada, verifique se ela é uma matriz
triangular superior.'''

n = int(input("Digite a ordem da matriz quadrada (n x n): "))
matriz = []

print("Digite os elementos da matriz: ")

for i in range(n):
    linha = []
    for j in range(n):
        coluna = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(coluna)
    matriz.append(linha)

print(matriz)
print()

triangular_superior = True
for i in range(1,n):
    for j in range(0,i):
        if matriz[i][j] != 0:
            triangular_superior = False
            break
    if not triangular_superior:
        break

if triangular_superior:
    print("A matriz é triangular superior.")
else:
    print("A matriz não é triangular superior.")
