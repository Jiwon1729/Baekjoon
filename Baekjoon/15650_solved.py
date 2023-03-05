import sys

N, M = map(int,sys.stdin.readline().split())
A = [[]for _ in range(1<<N)]
for i in range(1<<N):
    for k in range(N):
        if i&(1<<k)!=0:
            A[i].append(k+1)
A.sort()
for i in range(len(A)):
    if len(A[i])==M:
        print(" ".join(map(str,A[i])))


