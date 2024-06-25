import sys
from itertools import permutations

N,M = map(int,sys.stdin.readline().split())
Arr = list(map(int,sys.stdin.readline().split()))
Arr.sort()
ans=set()
for elem in permutations(Arr,M):
    ans.add(elem)
ans=list(ans)
ans.sort()
for elem in ans:
    print(*elem)