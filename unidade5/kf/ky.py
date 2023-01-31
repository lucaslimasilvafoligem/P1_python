def elimina_kyw(sentenca):
        palavranova = ''
        letras = ''
        for ini in sentenca:
            if ini in 'wWyYkK':
                letras += ini
            else:
                palavranova += ini
                
        return palavranova


