# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: calcular o valor das comissões a serem entregues aos vendedores.

vendedor = input("Qual é o nome do(a) vendedor(a)? ")
venda = float(input("Qual é o valor da venda? "))

if venda <= 500: 
    comissao = venda * 5 / 100 
    print(f"O valor da comissão para o(a) vendedor(a) {vendedor} é R$ {comissao:.2f}.")
elif venda > 500:
    comissao = venda * 10 / 100
    print(f"O valor da comissão para o(a) vendedor(a) {vendedor[0:5]} é R$ {comissao:.2f}.")
