# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: verificar se uma palavra é substring de outra.

def is_substring(str1, str2):
    pal = ''
    cont = 0
    achou = False
    for e in str1:
        if pal == str2:
            achou = True
            return achou
        if cont >= (len(str1) - len(str2)) + 1:
            break
        pal += e
        cont += 1
        for i in range(cont, len(str2) -1 + cont):
            if len(pal) <= len(str2):
                pal += str1[i]
            if len(pal) >= len(str2):
                if pal == str2:
                    achou = True
                    return achou
                else:
                    pal = ''

    return achou

