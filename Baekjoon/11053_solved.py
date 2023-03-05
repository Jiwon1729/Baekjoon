import sys
from bisect import bisect_left
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

D = [A[0]]
B = [0]
last=0
for i in range(1,N):
    if A[i]>D[last]:
        D.append(A[i])
        last+=1
        B.append(last)
    else:
        tmp = bisect_left(D,A[i],0,len(D))
        D[tmp] =A[i]
        B.append(tmp)
print(max(B)+1)
# print(D)
# print(A)

