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


lista = []

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
    sn = input('Quer continuar: [S/N] ').upper()
    if sn == 'N':
        break
meu_sort(lista)

print(lista)

