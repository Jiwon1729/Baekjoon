from itertools import combinations_with_replacement
import sys

N, M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
for ans in combinations_with_replacement(arr,M):
    print(*ans)