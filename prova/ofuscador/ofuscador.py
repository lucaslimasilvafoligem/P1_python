def regra_1(linha):
    primeira_regra = ""
    for caractere in linha:
        if 65 <= ord(caractere) <= 90: 
            primeira_regra += chr(ord(caractere) + 32)
        elif 97 <= ord(caractere) <= 122: 
            primeira_regra += chr(ord(caractere) - 32)
        else: 
            primeira_regra += caractere
    
    return primeira_regra

def troca_letras_por_numeros(caractere, segunda_regra):
    if caractere == "A" or caractere == "a": segunda_regra += "4"
    elif caractere == "B" or caractere == "b": segunda_regra += "8"
    elif caractere == "E" or caractere == "e": segunda_regra += "3"
    elif caractere == "G" or caractere == "g": segunda_regra += "6"
    elif caractere == "I" or caractere == "i": segunda_regra += "1"
    elif caractere == "L" or caractere == "l": segunda_regra += "7"
    elif caractere == "S" or caractere == "s": segunda_regra += "5"
    elif caractere == "O" or caractere == "o": segunda_regra += "0"
    else: segunda_regra += caractere

    return segunda_regra

def troca_numeros_por_letras(caractere, segunda_regra):
    if caractere == "4": segunda_regra += "A"
    elif caractere == "8": segunda_regra += "B"
    elif caractere == "3": segunda_regra += "E"
    elif caractere == "6": segunda_regra += "G"
    elif caractere == "1": segunda_regra += "I"
    elif caractere == "7": segunda_regra += "L"
    elif caractere == "5": segunda_regra += "S"
    elif caractere == "0": segunda_regra += "O"
    else: segunda_regra += caractere

    return segunda_regra

def regra_3(lista):
    terceira_regra = ""
    contador = 0
    for caractere in lista:
        if caractere == " ":
            terceira_regra += "*" * contador
            contador = 0
        else:
            terceira_regra += caractere
            contador += 1
    return terceira_regra

def ofuscador(linha):
    # REGRA 1
    primeira_regra = regra_1(linha)

    # REGRA 2
    segunda_regra = ""
    for caractere in primeira_regra:
        if  65 <= ord(caractere) <= 90 or 97 <= ord(caractere) <= 122:
            segunda_regra = troca_letras_por_numeros(caractere, segunda_regra)
        elif 48 <= ord(caractere) <= 57:
            segunda_regra = troca_numeros_por_letras(caractere, segunda_regra)
        else:
            segunda_regra += caractere

    # REGRA 3
    terceira_regra = regra_3(segunda_regra)

    return terceira_regra
