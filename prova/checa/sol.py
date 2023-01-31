# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.

num = input()
limite = float(input())

impar = 0
soma = 0
i = -1

while True:
    i += 1
    if i >= len(num):
        break
    soma += int(num[i])
    if int(num[i]) % 2 != 0:
        impar += 1
    if impar > 5:
        break
    if soma >= limite:
        break

if impar > 5:
    print(f'soma: {soma}\nnúmeros lidos: {i + 1} de {len(num)}\ncritério de parada: 6 ímpares')

elif soma >= limite:
    print(f'soma: {soma}\nnúmeros lidos: {i + 1} de {len(num)}\ncritério de parada: limite')
        
elif i >= len(num):
    print(f'soma: {soma}\nnúmeros lidos: {i} de {len(num)}\ncritério de parada: final da sequência')
