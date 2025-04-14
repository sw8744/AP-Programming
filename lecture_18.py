majors = {"CS": "Computer Science", "EE": "Electrical Engineering", "MAS": "Mathematical Science","ME": "Mechanical Engineering"}

d1 = dict()
d2 = {}

majors["PH"] = "Physic"
print(majors["PH"])

majors["PH"] = "Physics"
print(majors["PH"])

majors[0] = 0.001
print(majors)
print(len(majors))

del majors[0]
print(majors)
print(len(majors))

print("CS" in majors)
print("AI" in majors)

print(majors.keys())
print(majors.values())
print(majors.items())

for key in majors:
    print("%s is %s." % (key, majors[key]))

for key, value in majors.items():
    print("%s is %s." % (key, value))

import time
large_list = list(range(10000000))
large_set = set(large_list)

st = time.time()
for num in range(100000):
    if num not in large_list:
        print("What?!")
print("Running time for list: %f sec" % (time.time() - st))

st = time.time()
for num in range(100000):
    if num not in large_set:
        print("What?!")
print("Running time for set: %f sec" % (time.time() - st))