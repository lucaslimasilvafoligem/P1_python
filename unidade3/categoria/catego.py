# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: Um programa que com base na idade de um nadador determina em que categoria ele irá competir.
# Caso a idade seja inferior a 5 anos, "Não pode competir"
# Infantil A - 5 a 7 anos
# Infantil B - 8 a 10 anos
# Juvenil A - 11 a 13 anos
# Juvenil B - 14 a 17 anos
# Senior - Acima de 17 anos
nome = input()
idade = int(input())

if idade < 5:
    print(f"{nome}, {idade} anos, Não pode competir.")
elif idade >= 5 and idade < 8:
    print(f"{nome}, {idade} anos, Infantil A.")
elif idade >= 8 and idade < 11:
    print(f"{nome}, {idade} anos, Infantil B.")
elif idade >= 11 and idade < 14:
    print(f"{nome}, {idade} anos, Juvenil A.")
elif idade >= 14 and idade <= 17:
    print(f"{nome}, {idade} anos, Juvenil B.")
else:
    print(f"{nome}, {idade} anos, Senior.")

