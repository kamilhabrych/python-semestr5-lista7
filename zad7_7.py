import random

def sortuj(l):
    l.sort()
    print(l)

lista = []

for x in range(100):
        dlugosc = random.randint(3,8)
        slowo = ''
        for y in range(dlugosc):
            losowana_litera = random.randint(97,122)
            litera = chr(losowana_litera)
            slowo += litera
        lista.append(slowo)

print(lista)
sortuj(lista)
print()

lista2 = []
samogloski = ['a','i','e','u','o','y']

for i in range(100):
        dlugosc = random.randint(3,7)
        slowo = random.choice(samogloski)
        for j in range(dlugosc):
            losowana_litera = random.randint(97,122)
            litera = chr(losowana_litera)
            if litera not in slowo:
                slowo += litera
        lista2.append(slowo)

sortuj(lista2)