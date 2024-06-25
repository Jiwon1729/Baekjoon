# 230222
import sys
N = int(sys.stdin.readline())
R=[]
C=[]
for i in range(N):
    r,c = map(int,sys.stdin.readline().split())
    R.append(r)
    C.append(c)

mul = [[2**31 for _ in range(N)] for i in range(N)]
# mul[0][0]=0
for i in range(N):
    for j in range(i,-1,-1):
        if i==j:
            mul[i][j] = 0
        elif i-j==1:
            mul[i][j] = R[j]*C[j]*C[i]
        else:
            for k in range(i,j,-1):
                mul[i][j] = min(mul[i][k]+mul[k-1][j]+R[j]*C[k-1]*C[i],mul[i][j])

        # print(i,j,"i,j")
print(mul[N-1][0])