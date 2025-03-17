# 간단한 예시
if True:
    print("CS101 is my favorite course")

if False:
    print("Every CS101 student will receive an A+")

if 3 < 5:
    print("3 is less than 5")

else:
    print("3 is larger than 5")

# not 연산자 알아보기
print(not 3 < 5)

from cs1robots import *
import time

create_world(avenues=3, streets=3)
hubo = Robot(beepers=20)
sleep_time = 0.1
cnt = 0

def dance():
    for i in range(4):
        time.sleep(sleep_time)
        hubo.turn_left()

def move_or_turn():
    if hubo.front_is_clear():
        dance()
        global cnt
        cnt += 1
        time.sleep(sleep_time)
        hubo.move()
    else:
        hubo.turn_left()
        time.sleep(sleep_time)
        hubo.drop_beeper()

for i in range(20):
    move_or_turn()
print(cnt)

# pick a beeper
load_world("./worlds/beeper1.wld")
hubo = Robot()
sleep_time = 0.5

def move_and_pick():
    time.sleep(sleep_time)
    hubo.move()
    if hubo.on_beeper():
        time.sleep(sleep_time)
        hubo.pick_beeper()

for i in range(9):
    move_and_pick()
