from cs1robots import *

create_world(12, 12)
hubo = Robot(beepers=40)
ami = Robot(color="yellow")

def turn_right(robot):
    for i in range(3):
        robot.turn_left()

def goto_start(robot):
    for i in range(5):
        robot.move()
    robot.turn_left()
    robot.move()

def stairs_plant(robot, n):
    for i in range(n):
        robot.drop_beeper()
        robot.move()
        turn_right(robot)
        robot.move()
        robot.turn_left()

def stairs_harvest(robot, n):
    for i in range(n):
        robot.pick_beeper()
        robot.move()
        turn_right(robot)
        robot.move()
        robot.turn_left()

def diamond_plant(robot, n):
    for i in range(4):
        stairs_plant(robot, n)
        robot.turn_left()

def diamond_harvest(robot, n):
    for i in range(4):
        stairs_harvest(robot, n)
        robot.turn_left()

def plant_all(robot):
    for i in range(3):
        n = 5 - 2 * i
        diamond_plant(robot, n)
        robot.move()
        robot.move()

def harvest_all(robot):
    for i in range(3):
        n = 5 - 2 * i
        diamond_harvest(robot, n)
        robot.move()
        robot.move()

def happy_dance(robot):
    for i in range(102):
        robot.turn_left()

hubo.set_trace("blue")
hubo.set_pause(0.05)

ami.set_trace("red")
ami.set_pause(0.05)

goto_start(hubo)
plant_all(hubo)
happy_dance(hubo)

goto_start(ami)
harvest_all(ami)
happy_dance(ami)