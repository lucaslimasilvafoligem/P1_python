# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: Um programa que lê o comprimento, a largura e a profundidade de uma piscina e calcula o seu volume em litros. 

comprimento = float(input())
largura = float(input())
profundidade = float(input())

area = comprimento * largura * profundidade * 1000 

print(f"A piscina comporta {area:.2f} litros de água.")
