# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Objetivo: desenvolver um programa que a partir de quatro números inteiros não-negativos a, b, c e d e calcula o valor da expressão matemática dc - a - b - ca - d + bb + aad.

a  = int(input())
b  = int(input())
c  = int(input())
d  = int(input())

a1 = str(a)
b1 = str(b)
c1 = str(c)
d1 = str(d)
dc1 = d1 + c1
ca1 = c1 + a1
bb1 = b1 + b1
aad1 = a1 + a1 +d1
dc = int(dc1)
ca = int(ca1)
bb = int(bb1)
aad = int(aad1)
resultado = dc - a - b - ca - d + bb + aad

print(resultado)
