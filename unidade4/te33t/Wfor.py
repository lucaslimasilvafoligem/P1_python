lista = [1, 2, 3, 4, 5, 7, 8, 10]
UFCG = "UFcG"
frase = "Hoje é um dia chato."

for num in lista:
	print(num)

for letra in UFCG:
        print(letra)

for numm in lista:
    if numm % 2 == 0:
         print(numm)

for palavra in frase.split():
        print(palavra, end=" ")


