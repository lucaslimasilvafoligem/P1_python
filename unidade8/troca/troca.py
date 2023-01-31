def troca_valores(i, dados):
    temp = dados[i]
    dados[i] = dados[i + 1]
    dados[i + 1] = temp


def rotesq(array):
    #temp = array[0]
    for i in range(len(array) - 1):
        troca_valores(i, array)
        #if len(array) - 1 == i:
            #array[i] = temp


valores = [10, 20, 14, 17, 22, 9, 32]
rotesq(valores)
assert valores == [20, 14, 17, 22, 9, 32, 10]

