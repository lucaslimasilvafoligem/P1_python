# Lucas de Lima da Silva.
# Um programa que leia a quantidade de morangos colhidos e imprima quantas caixas serão completamente preenchidas.

morangos = int(input())

caixas = morangos // 400
resto = morangos % 400
perda = (resto * 100) / morangos

print(f"{caixas} caixa(s) completa(s) para embalar os morangos.")
print(f"{perda:.1f}% dos morangos serão perdidos.")

