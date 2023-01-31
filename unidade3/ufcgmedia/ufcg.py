# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: um pequeno programa que calcula a média final do estudante em uma disciplina.

media = float(input())

if media < 4 or media >= 7:
    print(f"média final: {media:.1f}")
elif media >= 4 and media < 7:
    notaf = float(input())
    resultado = (media * 6 + notaf * 4) / 10
    print(f"média final: {resultado:.1f}")

