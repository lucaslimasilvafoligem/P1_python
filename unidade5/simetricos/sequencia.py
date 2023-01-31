# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo:

num = int(input())

saida = ''
condi = ''
entr = 0
while condi != 'fim':
    seque = input().split()
    entr += 1
    condi = seque[0]
    if seque[0] == 'fim':
        break
    cont = 0
    cont2 = 0
    saida = ''
    for i in range(len(seque)):
        saida += seque[i]
        if len(seque) != i + 1:
            saida += ' '
        if int(seque[i]) > num:
            cont += 1
        if int(seque[i]) <= num:
            cont2 += 1

    if cont > cont2:
        print(f'Sequência {entr}: {saida}')


