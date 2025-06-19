import random
import time

def simple_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

large_list = list(range(20000))
random.shuffle(large_list)
st = time.time()
simple_sort(large_list)
print("Running time: %f sec" % (time.time() - st))