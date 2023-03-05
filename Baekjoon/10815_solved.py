import sys
N = int(sys.stdin.readline())
A = set(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))
answer=[]
for i in range(M):
    if B[i] in A:
        answer.append(0)
    else:
        answer.append(1)
print(" ".join(map(str, answer)))