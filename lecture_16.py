def bubbleSort(a):
    sorted = False
    while(not sorted):
        sorted = True
        for i in range(1, len(a)):
            if  a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                sorted = False
    return a

a = [5, 1, 4, 2, 8]
print(bubbleSort(a))

def sieve(n):
    candidates = list(range(2, n))
    i = 0
    # i : 확인된 소수에 대한 인덱스
    while i < len(candidates):
        prime = candidates[i]

        j = i + 1
        # j : 소수임을 확인해야 하는 숫자에 대한 인덱스
        while j < len(candidates):
            if candidates[j] % prime == 0:
                candidates.pop(j)
            else:
                j = j + 1
        i = i + 1
    return candidates

print(sieve(26))