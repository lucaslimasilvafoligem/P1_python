# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: Escreva uma função soma_intervalo(a, b) que recebe dois números inteiros, a e b, a <= b, e retorna a soma dos inteiros entre a e b, inclusive.

def soma_intervalo(a, b):
    soma1 = 0
    for i in range(a, b + 1):
        soma1 += i
    return soma1

