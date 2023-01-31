# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: desenvolver um programa que calcule, para o contribuinte, o valor do IPTU e as alternativas de pagamento.

areadcs = float(input("Área construída? "))
aliquota = float(input("Alíquota? "))

iptu = areadcs * aliquota + 35.00
unica = iptu - (iptu * 25 / 100)
seis = iptu - (iptu * 5 / 100)
seisdivision = seis / 6
dezdivision = iptu / 10
print(f"IPTU: R$ {iptu:.2f}\n")
print(f"Pagamento:\n1. Quota única. R$ {unica:.2f}\n2. Em 6 parcelas. Total: R$ {seis:.2f}\n   6 x R$ {seisdivision:.2f}\n3. Em 10 parcelas. Total: R$ {iptu:.2f}\n   10 x R$ {dezdivision:.2f}")

