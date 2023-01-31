lista = []
posi1 = ''
posi2 = ''
for i in range(5):
    numero = int(input(f'Digite o valor da posição {i}: '))
    lista.append(numero)
    if i == 0:
        maior = numero
        menor = numero
        posi1 = str(i)
        posi2 = str(i)
    elif numero >= maior:
        if numero == maior:
            posi1 += ' '
            posi1 += str(i)
        else:
            posi1 = ''
            maior = numero
            posi1 = str(i)
    elif numero <= menor:
        if numero == menor:
            posi2 += ' ' 
            posi2 += str(i)
        else:
            posi2 = ''
            menor = numero
            posi2 = str(i)

print(f'Você digitou os valores {lista}\nO maior valor digitado foi {maior} nas posições {posi1} \nO menor valor digitado foi {menor} nas posições {posi2}')

