from random import randint
computador = randint(0, 10)
print('Adivinhe o número de 0 até 10')
acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos...')

print(f'Acertou com {palpite} tentativas; Parabéns!')
