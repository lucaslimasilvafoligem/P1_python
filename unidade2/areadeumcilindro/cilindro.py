# Lucas de Lima da Silva.
# Objetivo: Cálculo da Superfície total de um Cilindro.

import math
print("Cálculo da Superfície de um Cilindro\n---")
diametro = float(input("Medida do diâmetro? "))
altura = float(input("Medida da altura? "))

raio = diametro / 2
areabase = math.pi * raio ** 2
arealateral = math.pi * 2 * raio * altura
areatotal = 2 * areabase + arealateral
print("---")
print(f"Área calculada: {areatotal:.2f}")
