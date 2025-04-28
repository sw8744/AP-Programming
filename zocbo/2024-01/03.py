from cs1robots import *

load_world("../../worlds/beeper1.wld")

hubo = Robot()

def dance():
    for i in range(4):
        hubo.turn_left()

def move_or_turn():
    while hubo.front_is_clear():
        if not hubo.on_beeper():
            dance()
            hubo.move()
        else:
            hubo.turn_left()
            hubo.turn_left()

move_or_turn()