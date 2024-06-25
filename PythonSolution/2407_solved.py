import sys
N, M= map(int, sys.stdin.readline().split())
answer = 1
for i in range(M):
    answer*=(N-i)
for i in range(M):
    answer//=(i+1)
print(int(answer))