from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print(f'Quem nasceu em {nasc}, tem {idade} anos, em {atual}.')

if idade == 18:
    print('deve se alisatar.')
elif idade < 18:
    salado = 18 - idade
    print(f'Você não tem 18 anos, faltam {saldo} para o alistamneto.')
else:
    saldo = idade - 18
    print(f'Você tem {idade}, ou seja, mais de 18 anos, já deveria ter se alistado a {saldo}.')

