# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: implemente a função tem_afinidade(l1, l2) que retorna verdadeiro caso os usuários possuam afinidade e falso, caso contrário.

def tem_afinidade(l1, l2):
    if len(l1) >= len(l2):
        menor = len(l2)
        maior = len(l1)
    else:
        menor = len(l1)
        maior = len(l2)
    afinidade = False
    cont = 0
    for i in range(menor):
        for ini in range(maior):
            if cont >= 3:
                afinidade = True
                return afinidade
            else:
                if maior == len(l1):
                    if l1[ini] == l2[i]:
                        cont += 1
                else:
                    if l1[i] == l2[ini]:
                        cont += 1
    return afinidade
    

