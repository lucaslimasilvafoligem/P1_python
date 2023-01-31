# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: Escreva a função calcula_digitos_verificacao(cpf) que calcula e retorna os dois dígitos de verificação de um número de CPF.

def calcula_digitos_verificacao(cpf):
    resposta = ''
    num = 11
    soma, soma1 = 0, 0
    for ini in cpf:
        soma1 += int(ini) * num
        num -= 1
        soma += int(ini) * num
    veri = soma * 10 % 11
    veri2 = (soma1 + 2 * veri) * 10 % 11
    if veri == 10:
        veri = 0
    if veri2 == 10:
        veri2 = 0
    resposta += str(veri) + str(veri2)
    return resposta

