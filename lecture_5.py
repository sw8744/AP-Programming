# Data Type 보기
print(type(3))
print(type(3.1415))
print(type("CS101 is fantastic"))
print(type(3 + 7j))
print(type(True))

n = None
print(type(n))

# 멤버 함수 (Method)
from cs1robots import *
create_world(avenues=5, streets=5)
hubo = Robot()
hubo.move()
hubo.turn_left()

b = "banana"
print(b.upper())

hubo = Robot("yellow")
hubo.move()
ami = hubo
ami.turn_left()
hubo.move()

hubo = Robot("blue")
hubo.move()
ami.turn_left()
ami.move()