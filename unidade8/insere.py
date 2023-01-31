from p1 import Array
from random import randint

def insere(a, index, valor):
    for i in range(9, index, -1):
        a[i] = a[i - 1]
    a[index] = valor

def pop(a, index):
    for i in range(index, 9):
        a[i] = a[i + 1]
    a[9] = None

a = Array(10)
for i in range(5):
    a[i] = randint(0, 9)
print(a)
insere(a, 3, 100)
print(a)
pop(a, 3)
print(a)


