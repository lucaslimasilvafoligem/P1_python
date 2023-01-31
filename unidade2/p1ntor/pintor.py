# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: Um programa que ajude um pintor de paredes a calcular o custo de seu serviço.

altura = float(input())
largura = float(input())

area = altura * largura
preço = 20 * area

print(f"R$ {preço:.2f}")
