import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
for elem in combinations_with_replacement(range(1, n+1), m):
  print(*elem)