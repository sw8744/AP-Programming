ta = ["JinYeong", "Jeongmin", "Minsuk", "Dohoo", "Sangjae", "Byung-Jun"]
ta.sort()
print(ta)

countries = ["Australia", "Austria", "Brazil", "Canada", "China", "Croatia", "Czech Republic", "Finland", "France", "Germany", "Great Britain",
    "Italy", "Japan", "Kazakhstan", "Latvia", "Netherlands", "Norway", "Poland", "Russia", "Slovakia", "Slovenia", "South Korea", "Sweden",
    "Switzerland", "Ukraine", "United States"]
gold = [0, 4, 5, 10, 3, 0, 2, 1, 4, 8, 1, 0, 1, 0, 0, 8, 11, 4, 13, 1, 2, 3, 2, 6, 1, 9]
silver = [2, 8, 0, 10, 4, 1, 4, 3, 4, 6, 1, 2, 4, 0, 2, 7, 5, 1, 11, 0, 2, 3, 7, 3, 0, 7]
bronze = [1, 5, 1, 5, 2, 0, 2, 1, 7, 5, 2, 6, 3, 1, 2, 9, 10, 1, 9, 0, 4, 2, 6, 2, 1, 12]

table = []
m = []

for i in range(len(countries)):
    m.append(gold[i] + silver[i] + bronze[i])
    table.append((m[i], gold[i], silver[i], bronze[i], countries[i]))

table.sort()
top_10 = table[-10:]
top_10.reverse()
for a, g, s, b, c in top_10:
    print(c, g, s, b)

def no_medals(countries, a1, b1):
    result = []
    for i in range(len(countries)):
        if a1[i] == 0 and b1[i] == 0:
            result.append(countries[i])
    return result

only_gold = no_medals(countries, gold, silver)
only_silver = no_medals(countries, silver, bronze)
only_bronze = no_medals(countries, bronze, gold)

only_one = only_gold + only_silver + only_bronze
print(only_one)

medals = [ ("Australia", 0, 2, 1), ("Austria", 4, 8, 5), ("Brazil", 5, 0, 1), ("Canada", 10, 10, 5), ("China", 3, 4, 2), ("Croatia", 0, 1, 0),
           ("Czech Republic", 2, 4, 2), ("Finland", 1, 3, 1), ("France", 4, 4, 7), ("Germany", 8, 6, 5), ("Great Britain", 1, 1, 2),
           ("Italy", 0, 2, 6), ("Japan", 1, 4, 3), ("Kazakhstan", 0, 0, 1), ("Latvia", 0, 2, 2), ("Netherlands", 8, 7, 9), ("Norway", 11, 5, 10),
           ("Poland", 4, 1, 1), ("Russia", 13, 11, 9), ("Slovakia", 1, 0, 0), ("Slovenia", 2, 2, 4), ("South Korea", 3, 3, 2),
           ("Sweden", 2, 7, 6), ("Switzerland", 6, 3, 2), ("Ukraine", 1, 0, 1), ("United States", 9, 7, 12)
    ]

def print_totals1():
    for country, g, s, b in medals:
        print(country + ":", g + s + b)

def print_totals2():
    for item in medals:
        print(item[0] + ":", sum(item[1:]))

print_totals1()
print_totals2()

def histogram():
    t = [0] * 13
    for item in medals:
        total = sum(item[1:])
        t[total // 3] += 1
    for i in range(13):
        print(str(3 * i) + "~" + str(3 * (i + 2)) + ":\t" + ("*" * t[i]))

histogram()
