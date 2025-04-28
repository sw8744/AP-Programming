def swap(a, b):
    b = a
    a = b
    return a, b

a, b = swap(1, 2)
print("a = ", a, "b = ", b)