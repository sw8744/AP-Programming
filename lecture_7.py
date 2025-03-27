from cs1media import *

red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
purple = (128, 0, 128)

img = create_picture(100, 100, purple)
img.show()
img.set_pixels(yellow)
img.show()

for i in range(4):
    print(i)

for i in range(7):
    print('*' * i)

for i in range(7):
    print(' ' * (6 - i) + '*' * i)

img = load_picture("photos/Ham.jpg")
w, h = img.size()
for y in range(h):
    for x in range(w):
        r, g, b = img.get(x, y)
        r, g, b = 255 - r, 255 - g, 255 - b
        img.set(x, y, (r, g, b))
img.show()

threshold = 100
white = (255, 255, 255)
black = (0, 0, 0)

img = load_picture("photos/Ham.jpg")
w, h = img.size()
for y in range(h):
    for x in range(w):
        r, g, b = img.get(x, y)
        if r > threshold:
            img.set(x, y, white)
        else:
            img.set(x, y, black)
img.show()

img = load_picture("photos/Ham.jpg")
img.show()
w, h = img.size()
for y in range(h):
    for x in range(w):
        r, g, b = img.get(x, y)
        v = (r + g + b) // 3
        img.set(x, y, (v, v, v))
img.show()