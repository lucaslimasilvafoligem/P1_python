- input: |
    2 2 2
    1 1 2 2 1
    8 9 1 0 2 4 4
    1 1 1 2 5 6
    fim
  output: |
    linha 2 inválida: 1 1 2 2 1
    linha 4 inválida: 1 1 1 2 5 6
    sequências lidas: 4 (inválidas: 2)

- input: |
    4 5 2 1 1
    5 7 8 9 2 3 10
    8 9 1 0 2 4 4 -1 7
    1 1 1 2 5 6
    fim
  output: |
    linha 1 inválida: 4 5 2 1 1
    linha 2 inválida: 5 7 8 9 2 3 10
    linha 4 inválida: 1 1 1 2 5 6
    sequências lidas: 4 (inválidas: 3)
