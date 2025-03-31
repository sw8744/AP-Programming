from cs1media import load_picture


def luma(p):
    r, g, b = p
    return int(0.213 * r + 0.715 * g + 0.072 * b)

white = (255, 255, 255)
black = (0, 0, 0)

def blackwhite(img, threshold):
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            v = luma(img.get(x, y))
            if v > threshold:
                img.set(x, y, white)
            else:
                img.set(x, y, black)

pict = load_picture("./photos/Ham.jpg")
blackwhite(pict, 100)
pict.show()