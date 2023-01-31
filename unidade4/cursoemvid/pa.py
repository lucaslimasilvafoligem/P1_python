termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

decimo = (termo1 + (10 - 1) * razao) + 1
for n in range(termo1, decimo, razao):
    print(n, end = " > ")
print('Acabou!')
