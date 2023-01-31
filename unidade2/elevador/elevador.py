# Lucas de Lima da Silva
# Objetivo: Um programa lê a capacidade máxima que um elevador pode transportar e o peso médio das pessoas que irão utilizar o elevador.

capacidade = int(input())
pesomedio = int(input())

pessoas = capacidade // pesomedio

print("O elevador pode transportar " + 
str(pessoas) + " pessoas com segurança.")
