# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: Desenvolver um programa que leia como inteiro o CPF dos vencedores e imprima esses CPFs com a formatação discutida acima, além da soma dos dois últimos dígitos de cada CPF.

vencedor1 = int(input())
vencedor2 = int(input())
vencedor3 = int(input())


nove1 = vencedor1 // 100 
dois = vencedor1 % 100 
a1 = dois // 10 
a2 = dois % 10
soma = a1 + a2

nove2= vencedor2 // 100
dois2 = vencedor2 % 100
a12 = dois2 // 10
a22 = dois2 % 10
soma2 = a12 + a22

nove3 = vencedor3 // 100
dois3 = vencedor3 % 100
a13 = dois3 // 10
a23 = dois3 % 10
soma3 = a13 + a23

print(f"{nove1}-{dois}\n{soma}")
print(f"{nove2}-{dois2}\n{soma2}")
print(f"{nove3}-{dois3}\n{soma3}")

