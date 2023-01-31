frase = input()

d = {}
for letra in frase:
    if letra in d:
        d[letra] += 1
    else:
        d[letra] = 1

print(d)
