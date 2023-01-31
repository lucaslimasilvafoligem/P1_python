# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: Desenvolver um programa que dadas as dimensões do vão (comprimento, largura e altura), calcule a quantidade de caixas de cerâmica necessárias para cobrir as paredes e o chão do ambiente.

import math

revestimento = float(input("Capacidade de revestimento? "))
comprimento = float(input("\n== Dados do vão a revestir ==\nComprimento? "))
largura = float(input("Largura? "))
altura = float(input("Altura? "))

fundo = comprimento * largura
lateral1 = comprimento * altura
frente = largura * altura
lateral2 = lateral1
traseira = frente
areatotal = fundo + lateral1 + lateral2 + frente + traseira
caixas = math.ceil(areatotal / revestimento)

print(f"\n== Resultados ==\nÁrea total a revestir: {areatotal} m2")
print(f"Número de caixas: {caixas}")
