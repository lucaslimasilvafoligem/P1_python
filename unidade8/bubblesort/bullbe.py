def troca_valores(i, dados):
    temp = dados[i]
    dados[i] = dados[i + 1]
    dados[i + 1] = temp


def bubblesort(dados):
    while True:
        swapped = False
        for i in range(0, len(dados) - 1):
            if dados[i] > dados[i+1]:
                troca_valores(i, dados)
                swapped = True
        if not swapped: break

