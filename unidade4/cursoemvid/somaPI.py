soma = 0
cont = 0

for num in range(1,7):
    n = int(input(f'Digite o {num} valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1

print(f'A soma de todos números pares é: {soma}; sendo {cont} deles pares.')       

