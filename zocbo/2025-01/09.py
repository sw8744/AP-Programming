from cs1robots import *
import time

create_world()

hubo = Robot("yellow")
hubo.move()
ami = hubo
ami.turn_left()
print("1 starts soon...")
time.sleep(1)
hubo.move() # 1
time.sleep(1)

hubo = Robot("blue")
hubo.move()
ami.turn_left()
print("2 starts soon...")
time.sleep(1)
ami.move() # 2