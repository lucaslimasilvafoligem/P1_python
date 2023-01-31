def troca_valores(i, dados):
    temp = dados[i]
    dados[i] = dados[i + 1]
    dados[i + 1] = temp


def bubblesort(dados):
    while True:
        for i in range(len(dados) - 1):
            if dados[i] > dados[i+1]:
                troca_valores(i, dados)
                swapped = True
        if not swapped: break


dados = [1, 2, 5, 4, 4.4, 8]
bubblesort(dados)
print(dados)
assert dados == [1, 2, 4, 4.4, 5, 8]

