def avg(data, start=0, end=None):
    if not end:
        end = len(data)
    return sum(data[start:end]) / float(end - start)

d = (1, 2, 3, 4, 5)

print(avg(end = None, data = d))
print(avg(d))
print(avg(d, 0, None))
print(avg(d, 1, 4))
print(avg(d, 1))