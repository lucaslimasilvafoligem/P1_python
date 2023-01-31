# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: um programa que recebe uma sequencia de números inteiros positivos e determina quantos desses números possui todos os cinco algarismos ímpares na sua formação. 

num = input().split()
impa = '13579'
cont = 0

for i in num:
    if i in impa:
        cont += 1

print(cont)
