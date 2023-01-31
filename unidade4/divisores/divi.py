# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: um programa que calcula os divisores próprios de um número inteiro maior do que zero.

num = int(input())
seque = num

for divisor in range(1, seque):
    if num % divisor == 0:
        print(divisor)

