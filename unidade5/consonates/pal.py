entr1 = int(input())
pal = []
somo = 0
soma = 0
fim = 0

for i in range(entr1):
    palavra = input()
    pal.append(palavra)

if len(pal[0]) > len(pal[-1]):
    maior = pal[0]
    menor = pal[-1]
    quanti = len(pal[-1])
    fim += 1

if len(pal[-1]) > len(pal[0]):
    maior = pal[-1]
    menor = pal[0]
    quanti = len(pal[0])
    fim += 1


if len(pal[0]) == len(pal[-1]):
    menor = pal[0]
    maior = pal[-1]
    quanti = len(pal[0])
    fim = 0

for ini in range(entr1):
    if ini != 0 and ini != (entr1 - 1):
        if len(pal[ini]) >= len(maior):
            somo += 1
        elif len(pal[ini]) <= len(menor):
            soma += 1

if fim == 0:
    print(f'Menor palavra dos extremos: {menor}, {maior} ({quanti} letras)')
    print(f'{soma} palavra(s) com tamanho menor')
    print(f'{somo} palavra(s) com tamanho maior')

if fim > 0:
    print(f'Menor palavra dos extremos: {menor} ({quanti} letras)')
    print(f'{soma} palavra(s) com tamanho menor')
    print(f'{somo} palavra(s) com tamanho maior')



#Saíav
#Na saída, seu programa deve imprimir a menor palavra dos extremos e os totais de palavras de tamanho menor e maior do que a menor palavra dos extremos. Caso as palavras dos extremos tenham o mesmo tamanho, elas devem sem impressas em conjunto. Veja o formato da saída nos exemplos de entrada e saída apresentados.
