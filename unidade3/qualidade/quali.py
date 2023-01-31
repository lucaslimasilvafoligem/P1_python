# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: desenvolver um programa que leia o peso (em kg) do produto antes de depois de descongelar e classifica o produto de acordo com as regras acima.

pesoantes = float(input())
pesodepois = float(input())

peso = pesodepois * 100 / pesoantes
resultado = 100 - peso
osnove = 9 * pesoantes / 100
osnove1 = osnove * 100 / pesoantes 
osquatro = 4 * pesoantes / 100
osquatro1 = osquatro * 100 / pesoantes
if resultado <= osquatro1:
    print(f"{resultado:.1f}% do peso do produto é de água congelada.\nProduto qualis A.")
elif resultado <= osnove1 and resultado > osquatro1:
    print(f"{resultado:.1f}% do peso do produto é de água congelada.\nProduto em conformidade.")
elif resultado > osnove1:
    print(f"{resultado:.1f}% do peso do produto é de água congelada.\nProduto não conforme.")

