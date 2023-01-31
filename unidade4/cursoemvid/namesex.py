media = 0
mediaidade = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print(f'-----{p} PESSOA -----')
    nome = input('Nome? ').strip()
    idade = int(input('Idade? '))
    sexo = input('Sexo? ').strip()
    media += idade
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
mediaf = media / 4

print(f'São {totmulher20} com 20 ou mais anos.')
print(f'O homem mais velho é o {nome} e ele tem {idade} anos.')
print(f'A medias das idades é {mediaf}.')

