n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 >= 0 and n2 >= 0 and n3 >= 0:
    soma = n1 + n2 + n3
    if soma > 100:
        print("A soma ultrapassou o limite")
    else:
        print(soma)
