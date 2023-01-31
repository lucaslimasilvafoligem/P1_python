# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: Escreva a função encontra_menores(num, lista) que receba um número inteiro e uma lista de inteiros. A função deve retornar o primeiro valor da lista que seja menor que o número ou -1, se não houver valor que atenda à condição.

def encontra_menores(num, lista):
    for i in range(len(lista)):
        if int(lista[i]) < num:
            resposta = int(lista[i])
            break
        if (len(lista) - 1) == i:
            resposta = -1
    return resposta

