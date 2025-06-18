'''Escreva uma função que dada uma matriz quadrada, verifique se ela é uma matriz
triangular inferior.'''

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

triangular_inferior = True
for i in range(n):
    for j in range(i +1,n):       #está conferindo se os elementos acima da dignonal principal são 0
        if matriz[i][j] != 0:
            triangular_inferior = False
            break
    if not triangular_inferior:
        break        

if triangular_inferior:
    print("A matriz é triangular inferior.")
else:
    print("A matriz não é triangular inferior.")
