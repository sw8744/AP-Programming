from cs1robots import *
import time

create_world()

turnTime = 0
hubo = Robot()

def turn_a():
    for i in range(2):
        hubo.turn_left()
        time.sleep(0.5)
        global turnTime
        turnTime += 1
        hubo.turn_left()
        time.sleep(0.5)
        turnTime += 1

def turn():
    turn_a()
    hubo.turn_left()
    global turnTime
    turnTime += 1
    time.sleep(0.5)

for i in range(5):
    turn()

print(turnTime // 4)