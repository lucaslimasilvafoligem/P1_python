from p1 import Array

def ordenado(a, num):
    for i in range(len(a))    
        if num <= a[i]:
            a.insert(i, num)
            return
    a.append(num)


a = []

while True:
    linha = input()
    if not linha: break
    num = int(linha)
    ordenado(a)
    print(a)

print('tchau')

