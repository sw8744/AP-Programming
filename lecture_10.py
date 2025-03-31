from cs1graphics import *
import time

def create_sun(radius, color):
    sun = Circle(radius)
    sun.setFillColor(color)
    sun.setBorderColor(color)
    sun.moveTo(100, 100)
    return sun

canvas = Canvas(400, 300)
canvas.setBackgroundColor("blue")

sun = create_sun(30, "yellow")
canvas.add(sun)

canvas.wait()
canvas.close()
