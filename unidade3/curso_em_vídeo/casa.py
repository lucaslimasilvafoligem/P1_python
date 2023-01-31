casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anos = int(input('Anos para pagar: '))

prestaçao = casa / (anos * 12) 
minimo = prestaçao * 100 / salario
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos, a prestação será de {prestaçao:.2f}')

if prestaçao <= minimo:
    print('Empréstimo pode ser CONCEDIDO.')
else: 
    print(f'Empréstimo NEGADO')
