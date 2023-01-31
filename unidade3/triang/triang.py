# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: um programa que a partir das medidas dos lados verifica se eles determinam um triângulo válido ou não.

a = float(input())
b = float(input())
c = float(input())

perimetro = a + b + c
if a <= 0 or b <= 0 or c <= 0:
    print("triangulo invalido.")
elif (b - c) < a < b + c and (a - c) < b < c + a and (a - b) < c < a + b:
    print(f"triangulo valido. {perimetro:.0f}")
else:
    print("triangulo invalido.")

