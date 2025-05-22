from cs1media import *

black = (0, 0, 0)
white = (255, 255, 255)

def hide_picture(img, bwimg, x1, y1):
    w, h = img.size()

    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            if r % 2 == 1:
                r = r - 1
            img.set(x, y, (r, g, b))

    w1, h1 = bwimg.size()
    for y in range(h1):
        for x in range(w1):
            r, g, b = img.get(x1 + x, y1 + y)
            if bwimg.get(x, y) == black:
                r = r + 1
            img.set(x1 + x, y1 + y, (r, g, b))

def restore_picture(img):
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            if r % 2 == 1:
                img.set(x, y, black)
            else:
                img.set(x, y, white)

secret = load_picture("./photos/haam_black.png")
img = load_picture("./photos/trees1.jpg")
hide_picture(img, secret, 100, 10)
img.save_as("./photos/trees1_haam.png")
img.show()
restore_picture(img)
img.show()
