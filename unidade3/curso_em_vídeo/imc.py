altura = float(input('Altura? em (Metros) '))
peso = float(input('Peso? em (KG) '))

imc = peso / (altura * altura)
print(f'{imc:.2f}')


if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc > 25 and imc < 30:
    print('Sobrepeso')
elif imc > 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')

