# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo:

def seleciona_primos(lista):
    primos = []
    for i in range(len(lista)):
        cont = 0
        for ini in range(1, i + 1):
            if lista[i] == 1:
                primos.append(lista[i])
                break
            elif lista[i] % ini != 0:
                cont += 1
                if cont == 2:
                    primos.append(lista[i])
    return primos
    
lista = [4, 5, 54, 11, 101, 7, 6, 8, 53, 59, 71, 40, 83, 90, 1000, 17, 10, 19, 1]
assert seleciona_primos(lista) == [5, 11, 101, 7, 53, 59, 71, 83, 19, 1]


