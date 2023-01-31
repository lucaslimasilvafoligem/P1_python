# Lucas de Lima da Silva.
# Um programa que, dado o lado do quadrado inscrito, calcule o perímetro e a área da circunferência.
import math

lado = float(input())

raio = lado / (2 ** 0.5) 
area = math.pi * raio ** 2
perimetro = 2 * math.pi * raio 

print(f"Perímetrco: {perimetro:.5f}")
print(f"Área: {area:.5f}")

