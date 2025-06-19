import random
import time

def merge(a1, a2):
    i1 = 0
    i2 = 0
    result = []
    while i1 < len(a1) and i2 < len(a2):
        if a1[i1] < a2[i2]:
            result.append(a1[i1])
            i1 += 1
        else:
            result.append(a2[i2])
            i2 += 1
    result += a1[i1:]
    result += a2[i2:]
    return result

def merge_sort(a):
    if len(a) <= 1:
        return a
    m = len(a) // 2
    a1 = a[:m]
    a2 = a[m:]
    l  = merge_sort(a1)
    r  = merge_sort(a2)
    lst = merge(l, r)
    return lst

large_list = list(range(20000))
random.shuffle(large_list)
st = time.time()
merge_sort(large_list)
print("Running time: %f sec" % (time.time() - st))