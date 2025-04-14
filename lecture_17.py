odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}
emptyset = set()
randomset = {4, 6, 2, 7, 5, 2, 3}

print(odds)
print(evens)
print(emptyset)
print(randomset)

gold = [0, 4, 5, 10, 3, 0, 2, 1, 4, 8, 1, 0, 1, 0, 0, 8, 11, 4, 13, 1, 2, 3, 2, 6, 1, 9]
print(gold)

goldset = set(gold)
print(goldset)
print(type(goldset))

print(set("Good morning!"))

print(3 in odds)
print(2 in odds)
for num in odds:
    print(num)

print(randomset)

randomset.add(9)
print(randomset)

randomset.remove(7)
print(randomset)

print(randomset.pop())
print(randomset)

print(randomset.intersection(odds))
print(randomset & odds)

print(randomset.union(evens))
print(randomset | evens)

print(randomset.difference(odds))
print(randomset - odds)

print(odds.difference(randomset))
print(odds - randomset)

print(randomset.difference(odds, evens))
print(randomset - odds - evens)