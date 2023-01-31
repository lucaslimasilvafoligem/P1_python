palavra1 = input()
palavra2 = input()

letras_distintas = []
for e in palavra1:
    cont = 0
    for i in range(len(palavra2)):
        if e != palavra2[i]:
            cont += 1
            if cont >= len(palavra2):
                letras_distintas.append(e)

print(len(letras_distintas))

