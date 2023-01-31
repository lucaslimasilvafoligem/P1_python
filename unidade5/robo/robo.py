x = 0
y = 0
l = 0

while True:
    com = input()
    for i in com:
        if i == 'C':
            cont = -1
            for e in com:
                cont += 1
                if cont >= 2:
                    if int(e) == 0:break
                    else:
                        y += int(e)
        elif  i == 'B':
            cont = -1
            for e in com:
                cont += 1
                if cont >= 2:
                    if int(e) == 0:break
                    else:
                        y -= int(e)
        elif i == 'E':
            cont = -1
            for e in com:
                cont += 1
                if cont >= 2:
                    if int(e) == 0:break
                    else:
                        x -= int(e)
        elif i == 'D':
            cont = -1
            for e in com:
                cont += 1
                if cont >= 2:
                    if int(e) == 0:break
                    else:
                        x += int(e)
    if x * 2 == y or x * 2 == y * -1 or x * -2 == y * -1 or x * -2 == y:
        l += 1
        break
    if int(e) == 0:
        break

if l != 0:
    print(f'Parabéns, conquista do portal ({x}, {y})')
elif l == 0:
    print('Fim de jogo')
