# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: um programa que, dado o registro de presença dos alunos, identifique o número de alunos que foram reprovados por falta.

reprovados = 0

while True:
    pres = input()
    faltas = 0
    ini = 0
    if pres == '-':
        break

    while ini < len(pres):
        if pres[ini] == 'f':
            faltas += 1
        ini += 1

        if faltas > 8:
            reprovados += 1
            break

print(f'{reprovados} aluno(s) reprovado(s) por falta.')

