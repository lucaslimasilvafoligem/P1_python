# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: verificar a quantidade de números identicos, suas posições e a porcentagem de idénticos

entr1 = input().split()
entr2 = input().split()
acum = 0

ini = 0
if len(entr1) > len(entr2):
    ini = len(entr2)
elif len(entr1) < len(entr2):
    ini = len(entr1)
else:
    ini = len(entr1)


for i in range(ini):
    if int(entr1[i]) == int(entr2[i]):
        acum += 1
        print(f'i = {i}: {entr1[i]}')

porc = len(entr1) + len(entr2)
cem = acum * 100 / porc
print(f'Valores coincidentes: {acum} ({cem:.0f}%)')

