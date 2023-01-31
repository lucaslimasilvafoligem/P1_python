# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo:

invalidado = 0
lidas = 0
while True:
    saida = '' 
    valores = input().split()
    lidas += 1
    if valores[0] == 'fim':
        lidas += -1
        break
    valido = 0
    invalido = 0
    for i in range(len(valores)):
        saida += (valores[i])
        if len(valores) != i + 1:
            saida += ' '

        if int(valores[i]) % 2 == 0:
            valido += 1
        else:
            invalido += 1
            
    if invalido > valido:
        invalidado += 1
        print(f'linha {lidas} inválida: {saida}')

print(f'sequências lidas: {lidas} (inválidas: {invalidado})')

