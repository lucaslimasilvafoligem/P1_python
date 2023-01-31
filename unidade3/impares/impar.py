# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: um programa que receba três números inteiros da entrada, calcule e imprima a soma deles. 

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 >= 0 and n2 >= 0 and n3 >= 0:
    soma = n1 + n2 + n3
    if soma > 100:
        print("A soma ultrapassou o limite")
    else:
        print(soma)
elif n1 < 0 and n2 >= 0 and n3 >= 0:
    soma = n2 + n3
    if soma > 100:
        print("A soma ultrapassou o limite")
    else:
        print(soma)
elif n1 >= 0 and n2 < 0 and n3 >= 0:
    soma = n1 + n3
    if soma > 100:
        print("A soma ultrapassou o limite")
    else:
        print(soma)
elif n1 >= 0 and n2 >= 0 and n3 < 0:
    soma = n1 + n2
    if soma > 100:
        print("A soma ultrapassou o limite")
    else:
        print(soma)
elif n1 < 0 and n2 < 0 and n3 >= 0:
    soma = n3
    if soma > 100:
        print("A soma ultrapassou o limite")
    else:
        print(soma)
elif n1 >= 0 and n2 < 0 and n3 < 0:
    soma = n1
    if soma > 100:
        print("A soma ultrapassou o limite")
    else:
        print(soma)
elif n1 < 0 and n2 >= 0 and n3 < 0:
    soma = n2
    if soma > 100:
        print("A soma ultrapassou o limite")
    else:
        print(soma)
#n1 < 0 and n2 < 0 and n3 < 0:
else:
    print("0")
