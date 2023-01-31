# Lucas de lima da Silva.
# Obetivo: cálcular o valor total dos ingressos.

adultos = int(input())
crianças = int(input())
ingresso = float(input())

preço = ingresso * adultos + ingresso * crianças / 2

print(f"Total: R$ {preço:.2f}")
