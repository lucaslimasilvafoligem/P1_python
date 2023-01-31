# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: um programa que verifica se um elemento está contido em uma lista de inteiros.

num = int(input())
nums = input().split()

sim = False
for elemento in nums:
    if num == int(elemento):
        sim = True
        break

if sim == True:
    print("sim")
else:
    print("não")    
