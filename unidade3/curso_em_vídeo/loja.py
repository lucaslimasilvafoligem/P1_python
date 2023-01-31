print('{:=^50}'.format('LOJAS GUANABARA'))
p = float(input('Valor da compra: R$'))
print('À VISTA DINHEIRO OU CHEQUE: 10% DE DESCONTO; DIGITE: [1]\nÀ VISTA CARTÃO: 5% DE DESCONTO; DIGITE: [2]\nEM ATÉ 2x NO CARTÃO: PREÇO NORMAL; DIGITE: [3]\n3x NO CARTÃO: 20% DE JUROS; DIGITE: [4]')
pag = int(input('Forma de pagamento? '))

if pag == 1:
    des = p - (p * 10 / 100)
    print(f'TOTAL IGUAL: R${des}.')
elif pag == 2:
    des = p - (p * 5 / 100)
    print(f'TOTAL IGUAL: R${des}.')
elif pag == 4:
    roub = p + (p * 20 / 100)
    print(f'TOTAL IGUAL: R${roub}.')
else:
    parce = p / 2
    print(f'TOTAL IGUAL: R${p}; DÍVIDIDO EM 2x DE R${parce}.')
