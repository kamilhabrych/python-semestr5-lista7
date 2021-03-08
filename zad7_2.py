a = 5
b = 10

def zmien(a,b):
    c = a
    a = b
    b = c
    print("a:",a)
    print("b:",b)

print("a:",a)
print("b:",b)
zmien(a,b)