lista = input().split()

soma = 0
for i in range(len(lista)):
    if i % 2 == 0:
        soma += int(lista[i])

print(soma)
