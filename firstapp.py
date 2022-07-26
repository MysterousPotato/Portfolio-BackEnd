while True:
    frase = str.split(input("Primera frase: "))
    segunda_frase = str.split(input("Segunda frase: "))

    print(frase)
    print(segunda_frase)

    total = 0
    for letras in frase:
        total += len(letras)

    total2 = 0
    for letras in segunda_frase:
        total2 += len(letras)


