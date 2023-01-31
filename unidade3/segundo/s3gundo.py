# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo:

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

print(f"Considerando os números {n1}, {n2}, {n3} e {n4}.")
if n1 >= n2 and n1 >= n3 and n1 >= n4:
    if n2 >= n3 and n2 >= n4: 
        print(f"O segundo maior numero é {n2}")
        if n3 >= n4:
            print(f"O segundo menor numero é {n3}")
        else:
            print(f"O segundo menor numero é {n4}")
    elif n3 >= n2 and n3 >= n4: 
        print(f"O segundo maior numero é {n3}")
        if n2 >= n4:
            print(f"O segundo menor numero é {n2}")
        else:
            print(f"O segundo menor numero é {n4}")
    elif n4 >= n2 and n4 >= n3:
        print(f"O segundo maior numero é {n4}")
        if n2 >= n3:
            print(f"O segundo menor numero é {n2}")
        else:
            print(f"O segundo menor numero é {n3}")
if n2 >= n1 and n2 >= n3 and n2 >= n4:
    if n1 >= n3 and n1 >= n4:
        print(f"O segundo maior numero é {n1}")
        if n3 >= n4:
            print(f"O segundo menor numero é {n3}")
        else:
            print(f"O segundo menor numero é {n4}")
    elif n3 >= n1 and n3 >= n4:
        print(f"O segundo maior numero é {n3}")
        if n1 >= n4:
            print(f"O segundo menor numero é {n1}")
        else:
            print(f"O segundo menor numero é {n4}")
    elif n4 >= n1 and n4 >= n3:
        print(f"O segundo maior numero é {n4}")
        if n1 >= n3:
            print(f"O segundo menor numero é {n1}")
        else:
            print(f"O segundo menor numero é {n3}")

if n3 >= n1 and n3 >= n2 and n3 >= n4:
    if n1 >= n2 and n1 >= n4:
        print(f"O segundo maior numero é {n1}")
        if n2 >= n4:
            print(f"O segundo menor numero é {n2}")
        else:
            print(f"O segundo menor numero é {n4}")
    elif n2 >= n1 and n2 >= n4:
        print(f"O segundo maior numero é {n2}")
        if n1 >= n4:
            print(f"O segundo menor numero é {n1}")
        else:
            print(f"O segundo menor numero é {n4}")
    elif n4 >= n1 and n4 >= n2:
        print(f"O segundo maior numero é {n4}")
        if n1 >= n2:
            print(f"O segundo menor numero é {n1}")
        else:
            print(f"O segundo menor numero é {n2}")

if n4 >= n1 and n4 >= n2 and n4 >= n3:
    if n1 >= n2 and n1 >= n3:
        print(f"O segundo maior numero é {n1}")
        if n2 >= n3:
            print(f"O segundo menor numero é {n2}")
        else:
            print(f"O segundo menor numero é {n3}")
    elif n2 >= n1 and n2 >= n3:
        print(f"O segundo maior numero é {n2}")
        if n1 >= n3:
            print(f"O segundo menor numero é {n1}")
        else:
            print(f"O segundo menor numero é {n3}")
    elif n3 >= n1 and n3 >= n2:
        print(f"O segundo maior numero é {n3}")
        if n1 >= n2:
            print(f"O segundo menor numero é {n1}")
        else:
            print(f"O segundo menor numero é {n2}")
