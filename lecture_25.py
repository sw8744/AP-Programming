def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(999))

def downup(w):
    print(w)
    if len(w) <= 1:
        return
    downup(w[:-1])
    print(w)

downup("CS101 is wonderful")

def sigma(n):
    if n <= 0:
        return 0
    else:
        return n + sigma(n - 1)

print(sigma(100))

def to_radix(n, b):
    if n < b:
        return str(n)
    s = to_radix(n // b , b)
    return s + str(n % b)

print(to_radix(675, 8))

