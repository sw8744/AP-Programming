import math
degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(math.sin(radians))
print(math.sqrt(2) / 2)

def print_twice(text):
    print(text)
    print(text)

print_twice("I love CS101")
print_twice(math.pi)

def student():
    name = "Hong Gildong"
    id = 20101234
    return name, id

name, id = student()
print(name)
print(id)

name = input("What is your name? ")
print("Welcome to CS101, " + name)

raw_n = input("Enter a positive integer> ")
n = int(raw_n)
for i in range(n):
    print('*' * i)