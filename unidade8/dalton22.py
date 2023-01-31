from p1 import Array

def insere(a, index, valor):
    for i in range(len(a) -1, index, -1):
        a[i] = a[i - 1]
    a[index] = valor


def ordenado(a, num):
    # if a[len(a) - 1] is not None:
    # return
    assert a[len(a) - 1] is None, ''
    for i in range(len(a)):
        if a[i] is None: break
        if num <= a[i]:
            insere(a, i, num)
            return
    
    a[i] = num
    

a = Array(10)

for i in range(9):
    ordenado(a, i * 10)

print(a)

while True:
    linha = input()
    if not linha: break
    num = int(linha)
    ordenado(a, num)
    print(a)

print('tchau')
