n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0

while opçao != 5:
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    opçao = int(input('Qual é a sua opção? '))
    if opçao == 1:
        val = n1 + n2
        print(f' A soma de ambos os valores corresponde a {val}.')
    elif opçao == 2:
        val = n1 * n2
        print(f'A multiplicção de ambos os valores correspondem a {val}.')
    elif opçao == 3:
        if n1 > n2:
            print(f'{n1} é maior.')
        elif n2 > n1:
            print(f'{n2} é maior.')
        else:
            print(f'{n1} e {n2} são iguais.')
    elif opçao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('...Fim...')
    else:
        print('Opção invalida; tente novamente.')
