n = int(input())

palavras = []
for i in range(n):
    palavra = input()
    palavras.append(palavra)
    
# ESSA PARTE É PARA ACHAR O MENOR ELEMENTO
menor = ""
if len(palavras[0]) > len(palavras[-1]): menor = palavras[-1]
else: menor = palavras[0]

# PARA CONTAR AS PALAVRAS MAIORES E OS MENORES
menores = 0
maiores = 0
for palavra in palavras:
    # CASO AS PALAVRAS NOS EXTREMOS TENHAM O MESMO TAMANHO, O PROGRAMA ENTRA NESSE IF AQUI
    if len(palavras[0]) == len(palavras[-1]) and palavra != palavras[0] and palavra != palavras[-1]:
        if len(palavra) < len(menor): menores += 1
        else: maiores += 1
    #CASO TENHAM TAMANHOS DIFERENTES O CÓDIGO ENTRA AQUI
    elif len(palavras[0]) != len(palavras[-1]) and palavra != menor:
        if len(palavra) < len(menor): menores += 1
        else: maiores += 1

# AQUI SE CONTRÓI A SAÍDA
saida = ""
if len(palavras[0]) == len(palavras[-1]): saida = f"{palavras[0]}, {palavras[-1]}"
else: saida = menor

print(f"Menor palavra dos extremos: {saida} ({len(menor)} letras)")
print(f"{menores} palavra(s) com tamanho menor")
print(f"{maiores} palavra(s) com tamanho maior")
