# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: um programa que conta as ocorrências em que o vizinho da direita de um elemento tem valor igual.

lista = input().split()

ocorrencias = 0
for i in range(len(lista)-1):
    if int(lista[i]) == int(lista[i+1]):
        ocorrencias += 1

print(ocorrencias)
