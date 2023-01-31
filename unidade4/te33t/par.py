lista = input().split()

soma = 0
for i in range(0, len(lista), 2):
        soma += int(lista[i])

print(soma)
