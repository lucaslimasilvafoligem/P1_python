# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: desenvolver um programa que verifica se um ano é bissexto ou não.

ano = int(input())

if ano % 400 == 0 and ano % 100 == 0:
    print(f"{ano} é bissexto")
elif ano % 100 == 0:
    print(f"{ano} não é bissexto")
elif ano % 4 == 0:
    print(f"{ano} é bissexto")
else:
    print(f"{ano} não é bissexto")

