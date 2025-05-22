import os
import cs1media

f = open("./text/planet.txt", "r")
s = f.readline()
print(s, len(s))

for l in f:
    s = l.strip()
    print(s, end=" ")
f.close()
print()

planets = []
f = open("./text/planet.txt", "r")
for line in f:
    planets.append(line.strip())
f.close()
print(planets)

f = open("./text/planet.txt", "r")
current = 0
earth = 0
for line in f:
    current += 1
    planet = line.strip().lower()
    if planet == "earth":
        earth = current
print("Earth is planet #%d" % earth)
f.close()

f = open("./text/planet.txt", "r")
earth = 0
for line in f:
    earth += 1
    planet = line.strip().lower()
    if planet == "earth":
        break
print("Earth is planet #%d" % earth)

f = open("./text/planetsc.txt", "r")
earth = 0
for line in f:
    planet = line.strip().lower()
    if planet[0] == "#":
        continue
    earth += 1
    planet = line.strip().lower()
    if planet == "earth":
        break
print("Earth is planet #%d" % earth)

f = open("text/words.txt", "r")
for line in f:
    word = line.strip()
    if len(word) > 18:
        print(word)
f.close()

f = open("text/words.txt", "r")
count = 0
for line in f:
    word = line.strip()
    if not "e" in word:
        count += 1
print("%d words have no 'e'" % count)
f.close()

def is_abecedarian(word):
    for i in range(1, len(word)):
        if word[i-1] > word[i]:
            return False
    return True

f = open("text/words.txt", "r")
for line in f:
    word = line.strip()
    if is_abecedarian(word):
        print(word)
f.close()

def three_doubles(word):
    s = ""
    for i in range(1, len(word)):
        if word[i-1] == word[i]:
            s = s + "*"
        else:
            s = s + " "
    return "* * *" in s

f = open("text/words.txt", "r")
for line in f:
    word = line.strip()
    if three_doubles(word):
        print(word)
f.close()

f = open("./text/test.txt", "w")
f.write("CS101 is fantastic\n")
f.close()

# 내가 한 것
exchange = []
for file in os.listdir("./text/ExchangeRate"):
    f = open("./text/ExchangeRate/" + file, "r")
    for line in f:
        data = line.split()
        date = data[0].split("/")
        exchange.append((date[0] + date[1] + date[2], int(1 / float(data[1]))))
    f.close()

print(exchange)

# 정답
years = list(range(1994, 2010))

def read_year(yr):
    fname = "./text/ExchangeRate/" + str(yr) + ".txt"
    f = open(fname, "r")
    data = []
    for l in f:
        date1, value1 = l.split()
        value = float(value1)
        value = int(1 / value)
        ys, ms, ds = date1.split("/")
        date = 10000 * int(ys) + 100 * int(ms) + int(ds)
        data.append((date, value))
    f.close()
    return data


def find_minmax(yr):
    minmax = [ (9999, 0) ] * 12
    data = read_year(yr)
    for d, v in data:
        month = (d // 100) % 100 - 1
        minr, maxr = minmax[month]
        if v < minr:
            minr = v
        if v > maxr:
            maxr = v
        minmax[month] = minr, maxr
    return minmax

for yr in  years:
    print("%4d: " % yr, end=" ")
    minmax = find_minmax(yr)
    for m in range(12):
        print("%4d/%-4d" % minmax[m], end=" ")
    print()

x_step = 5
min_y = 700
max_y = 2000
y_step = 0.5

def main():
    w = len(years) * 12 * x_step
    h = int((max_y - min_y) * y_step)
    p = cs1media.create_picture(w, h, cs1media.Color.white)

    for yr in years:
        x = (yr - years[0]) * 12 * x_step
        for y in range(h):
            p.set(x, y, cs1media.Color.gray)
        for won in range(min_y, max_y, 100):
            y = int((won - min_y) * y_step)
            for x in range(w):
                p.set(x, y, cs1media.Color.gray)

    for yr in years:
        minmax = find_minmax(yr)
        for m in range(12):
            x = ((yr - years[0]) * 12 + m) * x_step
            y1 = int((minmax[m][0] - min_y) * y_step)
            y2 = int((minmax[m][1] - min_y) * y_step)
            for y in range(h - y2, h - y1):
                p.set(x, y, cs1media.Color.red)

    p.show()
    p.save_as("./photos/krw.png")

main()