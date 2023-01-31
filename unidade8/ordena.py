from p1 import Array


def bs(a):
    for j in range(len(a)):
        houve_trocas = False
        for i in range(len(a) - 1 -j):
            if a[i] > a[i + 1]:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                houve_trocas = True

        if houve_trocas: return

a = Array(8)

a[0] = 80
a[1] = 70
a[2] = 40
a[3] = 50
a[4] = 20
a[5] = 60
a[6] = 90
a[7] = 10

print(a)
bs(a)
print(a)

