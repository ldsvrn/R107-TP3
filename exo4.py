def factorielleFor():
    nb = int(input("Entrez un nombre (for): "))
    factorielle = 1
    for i in range(1, nb + 1):
        factorielle *= i
    print(factorielle)


def factorielleWhile():
    nb = int(input("Entrez un nombre (while): "))
    temp = 1
    factorielle = 1
    while temp <= nb:
        factorielle *= temp
        temp += 1
    print(factorielle)


factorielleFor()
print("")
factorielleWhile()