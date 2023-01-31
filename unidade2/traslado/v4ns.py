# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: Desenvolver um programa que leia a quantidade de pessoas a serem transportadas e imprima quantas vans serão completamente preenchidas e também caso sobre uma quantidade de passageiros que não preencha por inteiro uma van, o programa considera que essas pessoas precisam de um transporte menor e deve imprimir essa quantidade em percentagem do total de passageiros.

pessoas = int(input())
capvans = int(input())

pvans = pessoas // capvans
semvan = pessoas % capvans
perda = semvan * 100 / pessoas

print(f"{pvans} van(s) completa(s).")
print(f"{perda:.2f}% dos passageiros não utilizarão vans.")
