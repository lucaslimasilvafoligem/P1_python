lista = input().split()

for i in range(len(lista)):
    if i == len(lista)-1:
        print("Último elemento da lista", end= " ")
    print(lista[i])
