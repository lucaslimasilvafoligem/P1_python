palavra = input("Digite apenas letras: ")
vogais = "aAeEiIoOuU"
palavras_sem_vogais = " "
palavras_com_vogais = " "

for letra in palavra:
    if letra not in vogais:
        palavras_sem_vogais += letra
        continue
    if letra in vogais:
        palavras_com_vogais += letra

print(palavras_sem_vogais)
print( palavras_com_vogais)
