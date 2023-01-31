def troca_valores(i, dados):
    temp = dados[i]
    dados[i] = dados[i + 1]
    dados[i + 1] = temp


def insere_ordenado_primeiro(lista):
    if len(lista) > 1:
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                troca_valores(i, lista)
            else:
                break


