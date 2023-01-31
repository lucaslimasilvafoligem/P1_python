# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: escreva a função inverte3a3(s) que recebe uma string s de caracteres e retorna uma string que corresponde à inversão 3 a 3 dos caracteres de s.

def inverte3a3(s):
    d = [] 
    nova = ''
    cont = 0
    for letra in s:
        nova += letra
        cont += 1
        if cont >= 3:
            d.append(nova)
            nova = ''
            cont = 0
    
    saida = ""
    for i in range(len(d) - 1, -1, -1):
        saida += d[i]
    
    return saida

assert inverte3a3("abcdef") == "defabc"
assert inverte3a3("abcdefghijkl") == "jklghidefabc"
