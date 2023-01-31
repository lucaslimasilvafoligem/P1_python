def busca(seq, valor):
    res = -1
    for i in range(len(seq)):
        if valor == seq[i]:
            return i
            
    return res


