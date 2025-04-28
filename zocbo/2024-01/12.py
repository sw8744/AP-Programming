five = set(range(5))
lows = {0, 1, 2, 3 ,4}
evens = {2, 4 ,6, 8}

lows.add(8)

print(lows.difference(evens))
print(lows.intersection(evens))
print(lows.issubset(five))
print(lows.issuperset(evens))
print(lows.union(five))