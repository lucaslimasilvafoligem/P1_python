def meu_remove(lista, e):
    for i in range(len(lista)):
        if lista[i] == e:
            lista.pop(i)
            break

def meu_remove(lista, e):
    for i in range(len(lista)-1, -1, -1):
        if lista[i] == e:
            lista.pop(i)
            break
