# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: desenvolver um programa que calcule o número de dias com base em segundos.

segundos = int(input())

minutos = segundos / 60
horas = minutos / 60
dias = horas / 24

print(f"{dias:.0f}")

