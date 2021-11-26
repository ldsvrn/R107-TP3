import random

rand = random.randint(0, 100)

while True:
    try:
        nb = int(input(f"Entrez un nombre entre 0 et 100 ({rand}): "))
        if not 0<=nb<=100:
            continue
            print("ERREUR: Entrez un nombre entier entre 0 et 100!")
    except ValueError:
        print("ERREUR: Entrez un nombre entier!")
        continue

    if rand < nb:
        print("Plus petit!")
    elif rand > nb:
        print("Plus grand!")
    else:
        print("Bravo!!")
        break