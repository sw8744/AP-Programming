a = "A"

def f(a):
    print(a)

def g():
    global a
    a = 5
    f(a + 1)
    print(a)

print(a)
f(5)
print(a)
g()
print(a)