# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: Escreva um programa que calcule se um determinado candidato quebrou ou não o recorde de quantidade comida de carne de sol do festival.

recorde = float(input())
valornovo = float(input())

if recorde > valornovo:
    print('recorde mantido')
elif recorde < valornovo:
    print(f'recorde quebrado ({valornovo:.2f} kg)')
else:
    print('recorde empatado')
