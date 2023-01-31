n = int(input('Digite um número inteiro: '))

soma = 0
cont = 0
for num in range(1, n + 1, 1):
    if num % 3 == 0:
        soma += num
        cont += 1
print(f'A soma dos números dívisiveis por 3 é: {soma:.0f}; com {cont} sendo a quantidade de números divididos')
