import sys

N, M = map(int, sys.stdin.readline().split())
A = set()
for i in range(N):
    A.add(str(sys.stdin.readline()))
answer = 0
B=set()
for i in range(M):
    B.add(str(sys.stdin.readline()))
answer=len(A&B)
print(answer)