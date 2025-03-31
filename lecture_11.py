def quadratic(a, b, c, x):
    quad_term = a * x ** 2
    lin_term = b * x
    return quad_term + lin_term + c

result = quadratic(2, 4, 5, 3)
print(result)

a = "Letter a"

def f(a):
    print("A = ", a)

def g():
    a = 7
    f(a + 1)
    print("A = ", a)

print("A = ", a)
f(3.14)
print("A = ", a)
g()
print("A = ", a)