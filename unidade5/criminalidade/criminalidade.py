# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: um programa que leia a média mensal estabelecida pela secretaria de segurança pública e várias sequencias de valores que representam a quantidade de ocorrências registradas por dia na delegacia. O programa deve imprimir na saída apenas as sequências cuja média mensal é maior que o estabelecido.

condi = 0
while condi == 0 : 
    medssp = float(input())
    while True:
        l = ''
        result = []
        sui = 0
        sequencia = input().split()
        if sequencia[0] == 'fim':
            condi += 1
            break
        soma = 0
        for ini in range(len(sequencia)):
            l += sequencia[ini]
            if (len(sequencia) - 1) > sui:
                l += ' '
                sui += 1
            ini = int(sequencia[ini])
            result.append(ini)
            soma += ini
        media = soma / len(sequencia)
        if media < (medssp / 2): 
            break  
        if media > medssp:
            print(l)
    condi += 1

