import sys
from itertools import combinations_with_replacement

N,M = map(int,sys.stdin.readline().split())
Arr = list(map(int,sys.stdin.readline().split()))
Arr=list(set(Arr))
Arr.sort()
for elem in combinations_with_replacement(Arr,M):
    print(*elem)