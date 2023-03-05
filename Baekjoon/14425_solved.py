import sys

N, M = map(int, sys.stdin.readline().split())
A = set()
for i in range(N):
    A.add(str(sys.stdin.readline()))
answer = 0
for i in range(M):
    tmp = str(sys.stdin.readline())
    if tmp in A:
        answer+=1
print(answer)