x = 0
y = 0
l = []

while True:
    com = input()
    l.appen(com)
    for i in com:
        if i == 'C':
            l.pop(0)
            l.pop(1)
            for i in com:
                x -= int(i)
        elif  i == 'B':
            l.pop(0)
            l.pop(1)
            for i in com:
                x -= int(i)
        elif i == 'E':
            l.pop(0)
            l.pop(1)
            for i in com:
                x -= int(i)
        elif i == 'D':
            for i in com:
                l.pop(0)
                l.pop(1)
                for i in com:
                    x -= int(i)
