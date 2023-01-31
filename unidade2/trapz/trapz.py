# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: Escrever um programa que lê a altura de um trapézio da entrada e imprime sua área com pelo menos duas casas.

paralelo1 = float(input())
paralelo2 = float(input())
altura = float(input())

area = (paralelo1 + paralelo2) * altura / 2

print(f"{area:.2f}")
