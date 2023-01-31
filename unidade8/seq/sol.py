# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo:

pares = []
impares = []

while True:
    num = int(input())
    if num % 2 == 0:
        pares.append(num)
    if num % 2 != 0:
        impares.append(num)
    if len(pares) - len(impares) > 2:
        print('PARES em maior quantidade')
        break
    if len(impares) - len(pares) > 2:
        print('IMPARES em maior quantidade')
        break

print('PARES:')
for i in range(len(pares)):
    print(pares[i])
    
print('IMPARES:')
for i in range(len(impares)):
    print(impares[i])
