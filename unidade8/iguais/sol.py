# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: 

seq1 = input().split()
seq2 = input().split()

if len(seq1) >= len(seq2):
    menor_seq = len(seq2)

else:
    menor_seq = len(seq1)

for i in range(menor_seq):
    if int(seq1[i]) == int(seq2[i]):
        print(f'{i + 1}: {seq1[i]}')
