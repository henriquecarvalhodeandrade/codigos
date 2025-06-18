import time

'''Escreva uma função que calcule o enésimo número de Fibonacci de forma recursiva,
a partir de um valor fornecido pelo usuário. Além disso, crie também uma função
iterativa do Fibonacci e compare a quantidade de somas e a de tempo de execução.'''

#FIBONACCI COM RECURSÃO

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
    
while True:
    try:
        n = int(input("Qual elemento de Fibonacci você gostaria de saber: "))
        if n < 0:
            print("Digite um número inteiro não negativo: ")
        else:
            print(f"O número [{n}] de Fibonacci é:  = {fibonacci_recursivo(n)}")
            break
    except ValueError:
        print("Opção invalida. Digite um número inteiro positivo: ")

print()
        

#FIBONACCI SEM RECURSÃO

def fibonacci_iterativo(n):
    if n == 0:
        return 0,0
    elif n == 1:
        return 1,0
    
    a = 0
    b = 1
    soma = 0

    for n in range(2, n + 1):
        a,b = b, a + b
        soma += 1
    return b,soma

while True:
    try:
        n = int(input("Qual elemento de Fibonacci você gostaria de saber: "))
        if n < 0:
            print("Digite um número inteiro não negativo.")
        else:
            break
    except ValueError:
        print("Opção inválida. Digite um número inteiro positivo.")

    print()    
valor,soma = fibonacci_interativo(n)
print("O elemento de Fibonacci é: ",valor)
print("A quantidade de somas é: ", soma)



    




