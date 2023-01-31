# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo:

palavra1 = input()
palavra2 = input()

lista2 = []
lista1 = []
cont = 0
xi = 0

print("Letras coincidentes")
if len(palavra1) >= len(palavra2):
    xi += 1
    for ini in palavra2:
        lista2 += ini
    
    for ina in palavra1:
        lista1 += ina
    
    for i in range(len(lista2)):
        if lista2[i] == lista1[i]:
            cont += 1
            c = i + 1
            print(f"'{lista2[i]}' na posição {c}")
    if xi > 0:
        porcem = cont * 100 / (len(lista1) + len(lista2)) 
        print(f"Total de letras coincidentes: {cont} ({porcem:.0f}%)")

elif len(palavra2) >= len(palavra1):
    xi += 1
    for ina in palavra1:
        lista1 += ina
    
    for ini in palavra2:
        lista2 += ini
    
    for i in range(len(lista1)):
        if lista1[i] == lista2[i]:
            cont += 1
            c = i + 1
            print(f"'{lista1[i]}' na posição {c}")
    if xi > 0:
        porcem = cont * 100 / (len(lista1) + len(lista2)) 
        print(f"Total de letras coincidentes: {cont} ({porcem:.0f}%)")
