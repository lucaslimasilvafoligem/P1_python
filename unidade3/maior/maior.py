# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: Usando apenas condicionais, escreva um programa que lê e ordena 3 números inteiros.

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 >= n2 >= n3:
    print(n3, n2, n1)

elif n1 >= n3 >= n2:
    print(n2, n3, n1)

elif n2 >= n1 >= n3:
    print(n3, n1, n2)

elif n2 >= n3 >= n1:
    print(n1, n3, n2)

elif n3 >= n2 >= n1:
    print(n1, n2, n3)

elif n3 >= n1 >= n2:
    print(n2, n1, n3)

