# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula:
# Objetivo:

def meu_in(elemento, sequencia):
    for e in sequencia:
        if e == elemento+1:
            return True
    return False


def trinca(digitos):
    trinca = []
    for numero in digitos:
        if meu_in(numero, digitos):     
            if meu_in(numero+1, digitos):
                trinca.append(numero)
                trinca.append(numero+1)
                trinca.append(numero+2)

    for numero in trinca: 
        for i in range(len(digitos)-1, -1, -1):
            if numero == digitos[i]:
                digitos.pop(i)


digitos= [1,7,2,8,5,3,9]
assert trinca(digitos) == None
assert digitos == [5]

digitos2= [1,8,5,3,9]
assert trinca(digitos2) == None
assert digitos2 == [1,8,5,3,9] 

digitos3 = [1,2,3]
assert trinca(digitos3) == None
assert digitos3 == []

