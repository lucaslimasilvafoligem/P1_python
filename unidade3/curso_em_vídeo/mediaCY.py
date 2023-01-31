n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota: '))

nota = (n1 + n2) / 2 

if nota < 5:
    print('Reprovado.')
elif nota >= 5 and nota < 7: 
    print('Recuperação.')
else:
    print('Aprovado.')
