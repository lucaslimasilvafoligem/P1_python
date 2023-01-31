entr = int(input())
soma = 0
soma2 = 0
c = []

for i in range(entr): 
    n = int(input())
    soma += n
    c.append(n)
    
media = soma / entr

for ini in range(len(c) -1, -1, -1):
    if c[ini] < media:
        soma2 += c[ini]
    else:
        soma2 += c[ini]
        break

print(soma2)
