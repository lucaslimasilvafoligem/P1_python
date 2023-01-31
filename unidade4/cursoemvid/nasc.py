mais = 0
menos = 0
for idade in range(1, 8):
    nasc = int(input('Digite o ano de nascimento: '))
    v = 2021 - nasc
    if v >= 21:
        mais += 1
        print(f'Mais de 18: {mais}')
    else:
        menos += 1
        print(f'Menos de 18: {menos}')
