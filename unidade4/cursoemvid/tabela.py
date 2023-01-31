n = int(input('Digite um número inteiro: '))

print('=' * 16)
print(f'A tbela de {n} é:')
for num in range(11):
    mult = n * num
    print(f'{n} x {num:2} = {mult}')

