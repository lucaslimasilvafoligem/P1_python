# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: desenvolver um programa que a partir do número de gols dos dois times determina quem foi o time vencedor.

Campinense = int(input())
Treze = int(input())

if Campinense > Treze:
    print("Campinense")
elif Treze > Campinense:
    print("Treze")
else:
    print("Empate")
