def sieve(n):
    candidates = list(range(2, n)) # Answer : list(range(2, n))
    i = 0
    while i < len(candidates):
        prime = candidates[i]
        j = i + 1
        while j < len(candidates):
            if candidates[j] % prime == 0:
                candidates.pop(j)
            else:
                j = j + 1
        i = i + 1
    return candidates

print(sieve(10))