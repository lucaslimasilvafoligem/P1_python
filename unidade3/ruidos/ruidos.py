# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: um sistema de detecção de ruídos em horários não permitidos (22h às 6h). 

num = input().split()
cont = 0

for i in range(len(num)):
    if num % 2 != 0:
        cont += 1

print(cont)

