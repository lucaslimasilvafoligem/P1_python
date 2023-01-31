# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo:

def is_substring_expr(str1,str2):
    pal1 = ''
    pal2 = ''
    tst1 = ''
    tst2 = ''
    condi = 0
    cont = 0
    r = False

    for i in str2:
        if i == '*':
            condi += 1
        if i != '*' and condi == 0:
            pal1 += i
        if condi > 0 and i != '*':
            pal2 += i
    for ini in str1:
        cont += 1
        if cont <= len(pal1):
            tst1 += ini
            if tst1 == pal1:
                r1 = True
            else:
                r1 = False
        if cont > len(str1) - len(pal2):
            tst2 += ini
            if tst2 == pal2:
                r2 = True
            else:
                r2 = False
    if r1 == True and r2 == True:
        r = True
    return r


