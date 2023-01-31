
def ultimo_indice(num, lista):
    inde = -1
    for i in range(len(lista)):
        if num == lista[i]:
            inde = i
    
    return inde

assert ultimo_indice(2, [15,2,13,11,14,2]) == 5
assert ultimo_indice(42, [15,2,13,11,14,2]) == -1
