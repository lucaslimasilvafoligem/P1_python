# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: um programa que imprima todos os números da seguinte sequência.

inicio = 15.2
fim = -5.8 - 1.5
delta = -1.5

repeticoes = int(((fim - inicio) / delta))
for flooat in range(repeticoes): 
    numero = inicio + (flooat * delta)
    print(f"{numero:.1f}")

