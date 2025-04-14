countries = ["Australia", "Austria", "Brazil", "Canada", "China", "Croatia", "Czech Republic", "Finland", "France", "Germany", "Great Britain",
    "Italy", "Japan", "Kazakhstan", "Latvia", "Netherlands", "Norway", "Poland", "Russia", "Slovakia", "Slovenia", "South Korea", "Sweden",
    "Switzerland", "Ukraine", "United States"]
gold = [0, 4, 5, 10, 3, 0, 2, 1, 4, 8, 1, 0, 1, 0, 0, 8, 11, 4, 13, 1, 2, 3, 2, 6, 1, 9]
silver = [2, 8, 0, 10, 4, 1, 4, 3, 4, 6, 1, 2, 4, 0, 2, 7, 5, 1, 11, 0, 2, 3, 7, 3, 0, 7]
bronze = [1, 5, 1, 5, 2, 0, 2, 1, 7, 5, 2, 6, 3, 1, 2, 9, 10, 1, 9, 0, 4, 2, 6, 2, 1, 12]

print(countries[0])
print(countries[21])
print(gold[21])
print(countries[-1])
print(countries[-5])

korea = ["Korea", "KR", 3, 3, 2]
print(korea[1])
print(korea[2])

korea = ["Korea", "KR", (3, 3, 2)]

nobles = ["helium", "none", "argon", "krypton", "xenon"]
nobles[1] = "neon"
print(nobles)

nobles.append("radon")
print(nobles)

totals = []
for i in range(len(countries)):
    medals = gold[i] + silver[i] + bronze[i]
    totals.append((medals, countries[i]))

print(totals)