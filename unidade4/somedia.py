n = input().split()
soma = 0
soma2 = 0

for i in range(len(n)):
    soma += int(n[i])
    media = soma / len(n)

for a in range(len(n)):
    if soma2 < media:
        soma2 += int((n[a]))

print(media, soma2)
