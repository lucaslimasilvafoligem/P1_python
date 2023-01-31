# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: Escreva uma função chamada maioridade_penal que informe o nome das pessoas que atingiram a maioridade penal (idade >= 18).

def maioridade_penal(nomes, idades):
    nomes = nomes.split()
    idades = idades.split()
    maioridade = ''
    cont = 0
    for i in range(len(nomes)):
        if int(idades[i]) >= 18:
            if cont == 0:
                maioridade += nomes[i]
            cont += 1
            if (cont - 1) > 0:
                maioridade += ' '
                maioridade += nomes[i]
    return maioridade

