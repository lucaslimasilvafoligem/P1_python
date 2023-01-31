# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: Escreva a função soma_simetricos(valores) que recebe uma lista com N valores inteiros e retorna uma outra lista contendo as somas de todos os valores que ocupem posições simétricas da lista: primeiro com o último, segundo com o penúltimo, e assim por diante. Se a lista tiver um número ímpar de valores o valor central deve ser o último valor da lista retornada.

def soma_simetricos(valores):
    somados = []
    i2 = -1
    for i in range(len(valores)-1, -1, -1):
        i2 += 1
        if i2 == i:
            somados.append(valores[i2])
            break
        soma = valores[i] + valores[i2]
        somados.append(soma)
        if len(somados) == len(valores)/2:
            break
    return somados
        
