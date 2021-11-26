import time

def rebourdFor():
    nb = int(input("Entrez un nombre (for): "))
    for i in range(nb + 1):
        print(nb - i, end="! ")
        time.sleep(1)

def rebourdWhile():
    nb = int(input("Entrez un nombre (while): "))
    temp = 0
    while temp <= nb:
        print(nb - temp, end="! ")
        temp += 1
        time.sleep(1)

rebourdFor()
print("")
rebourdWhile()