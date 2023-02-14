def eratosthenes(n = 1000000):
    n+=1
    sieve = [True] * (n)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

# 비트마스크를 이용한 개선: https://shoark7.github.io/programming/algorithm/sieve-of-eratosthenes-bitmask