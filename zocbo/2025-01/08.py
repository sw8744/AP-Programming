from cs1graphics import *
import time

canvas = Canvas(600, 200)
sq = Square(10)
sq.setFillColor("blue")
sq.moveTo(10, 100)
canvas.add(sq)

for i in range(360):
    sq.move(1, 0)
    sq.rotate(1)
    time.sleep(0.1)