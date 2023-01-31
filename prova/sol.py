invalidado = 0
linha = 0
while True:
    valores = input().split()
    linha += 1
    if valores[0] == 'fim':
        break
    valido = 0
    invalido = 0
    for i in range(len(valores)):
        if valores[i] % 2 == 0:
            valido += 1
        else:
            invalido += 1
            invalidado += 1

    if invalido > valido:
        print(f'linha {linha} inválida: {valores}')

print(f'sequências lidas: {linha} (inválidas: {invalidado})')

