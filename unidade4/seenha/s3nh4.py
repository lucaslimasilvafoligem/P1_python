# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: criptografar uma senha trocando a, e, i e o por: 4, 3, 2, 0 respectivamente, com exceção da primeira letra que permanecerá sendo a mesma.

palavra = input()
novastrig = ""
soma = 0
soma1 = 0
for letra in palavra:
    if letra == palavra[0] and soma1 == 0:
        novastrig += letra
        soma1 += 1
    elif letra == "A" or letra == "a": 
        novastrig += "4"
        soma += 1
    elif letra == "E" or letra == "e":
        novastrig += "3"
        soma += 1
    elif letra == "I" or letra == "i":
        novastrig += "1"
        soma += 1
    elif letra == "O" or letra == "o":
        novastrig += "0"
        soma += 1
    else:
        novastrig += letra

print(f'{novastrig} ({soma} troca(s))')

