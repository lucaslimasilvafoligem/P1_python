def troca_valores(posicao_fila, i, fila):
    temp = fila[posicao_fila]
    fila[posicao_fila] = fila[i]
    fila[i] = temp


def idosos_inicio(fila):
    posicao_fila = 0
    for i in range(len(fila)):
        if fila[i] >= 60:
            troca_valores(posicao_fila, i, fila)
            posicao_fila += 1



