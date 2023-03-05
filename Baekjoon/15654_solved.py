from itertools import permutations
import sys

N, M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
for ans in permutations(arr,M):
    print(*ans)