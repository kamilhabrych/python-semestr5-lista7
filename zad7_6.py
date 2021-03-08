def sortuj(l):
    l.sort()
    print(l)

zdanie = str(input("Podaj zdanie:"))

l = zdanie.split()

print(l)
sortuj(l)
print(sorted(l,key=len))