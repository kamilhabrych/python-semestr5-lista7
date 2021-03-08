import random

l = []

for i in range(10):
    n = random.randint(0,100)
    l.append(n)

print(l)

def sortuj(l):
    l.sort()
    print(l)

sortuj(l)

lista = ['Politechnika','Opolska','Python','Języki','Programowania','Wysokiego','Poziomu']

sortuj(lista)