def meu_slice(lista, começo, fim):
    nova_lista = []
    for i in range(começo, fim):
        nova_lista.append(lista[i])

    return nova_lista

def meu_sort(lista):
    tamanho = len(lista)
    listanova = []
    while len(listanova) < tamanho:
        maior = lista[0]
        ind = 0
        for i in range(len(lista)):
            if lista[i] > maior:
                maior = lista[i]
                ind = i
        lista.pop(ind)
        listanova.append(maior)
    return listanova

def noves_fora(lista):
    novesfora = [lista]
    resta = 0
    if len(lista) == 1:
        if lista[0] < 9:
            resta = lista[0]
            return resta, novesfora
        else:
            novesfora.append([0])
            return resta, novesfora
    while True:
        if len(lista) == 1:
            if lista[0] < 9: break
            else:
                novesfora[1] = [0] 
                resta = 0
                break

        resta = (lista[0] + lista[1]) % 9
        lista = [resta] + meu_slice(lista, 2, len(lista))
        lista = meu_sort(lista)
        novesfora.append(lista)

    return resta, novesfora
