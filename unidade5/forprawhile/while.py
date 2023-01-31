# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: Subistituir um for por while

fator = int(input())

i = -1
while True:
    if i > 9:
        break
    i += 1
    produto = i * fator
    print(f"{fator}  x {i:2}  = {produto:3}")
