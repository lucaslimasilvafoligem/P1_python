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
    l2 = []
    l = len(lista)
    for i in range(l):
        lista = meu_sort(lista)
        l2.append(lista)
        if len(lista) == 1:
            print(l2)
            return res, l2
        res = lista[0] + lista[1]
        if res > 9:
            res = res - 9
            if i == 0:
                lista.pop(0)
                lista[0] = res
            else:
                lista.pop(1)
                lista[0] = res
        else:
            if i == 0:
                lista.pop(0)
                lista[0] = res
            else:
                lista.pop(1)
                lista[0] = res

    return res, l2

print(noves_fora([9, 7, 5, 4, 3, 1])
assert noves_fora([9, 7, 5, 4, 3, 1]) == (2, [[9, 7, 5, 4, 3, 1], 
                                              [7, 5, 4, 3, 1], 
                                              [4, 3, 3, 1], 
                                              [7, 3, 1], 
                                              [1, 1], 
                                              [2]])
