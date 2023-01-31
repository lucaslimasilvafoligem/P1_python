a = int(input('valor de a: '))
b = int(input('Valor de b: '))
c = int(input('Valor de c: '))

if a <= 0 or b <= 0 or c <= 0:
    print('Trinagulo invalido.')
elif (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('Triangulo valido.')
    if a == b and b == c:
        print('Trianlgulo Equilátero')
    elif a != b and b != c and c != a:
        print('Triangulo Escaleno')
    else:
        print('Isóceles')
else:
    print('Triangulo Invalido')

