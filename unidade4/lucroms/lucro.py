# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: desenvolver um programa que elia na mesma linha receita e despesas e calcule o lucro.

MES =['jan', 'fev', 'mar', 'abr',
      'mai', 'jun', 'jul', 'ago', 
      'set', 'out', 'nov', 'dez' ]
        
receitas, despesas = [], []

for i in range(12):
    linha = input().split()
    receita, despesa = float(linha[0]), float(linha[1])
    receitas.append(receita)
    despesas.append(despesa)

for i in range(12):
    lucro = receitas[i] - despesas[i]
    print(f'{MES[i]} {lucro:4.1f}')
