def delta(a, b, c):
    d = b ** 2 - 4 * a * c
    return d

a1, b1, c1 = 6, 8, 2
a2, b2, c2 = 9, 24, 16
a3, b3, c3 = 1, -2 , 4

print(delta(a1, b1, c1))
print(delta(a2, b2, c2))
print(delta(a3, b3, c3))

def print_ola():
    nome = input()
    saida = 'Olá,' + nome + '!'
    print(saida)

def pa(a0, n, razao = 1):

    for i in range(n):
        termo = a0 + i * razao
        print(termo)
