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

# Unionfind:  두 노드를 같은 집합으로 묶어주고 확인할 수 있게 함
parents = [i for i in range(5)]
def find(x):
    if x == parents[x]:
        return x
    else:
        y = find(parents[x])
        parents[x] = y
        return y

def union(x, y, indx):
    global endgame
    x = find(x)
    y = find(y)
    if x != y: # cycle이 아닐 시
        parents[max(x,y)] = min(x,y)
    elif endgame == 0:
        endgame = indx