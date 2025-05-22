from cs1media import *
img = load_picture("./서4.jpg")
w, h = img.size()
for y in range(h // 2):
    for x in range(w):
        r, g, b = img.get(x, y + h // 2)
        img.set(x, y, (r, g, b))
img.show()