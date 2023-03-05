import sys
import copy
N = int(sys.stdin.readline())
chess = []

for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    if N%2 == 0:
        tmp.append(0)
    chess.append(tmp)
if N%2 ==0:
    tmp=[0 for _ in range(N+1)]
    chess.append(tmp)
    N=N+1
answer1 = 0
answer2 = 0
# print(chess)
def dfs(mat,i,j,cnt):
    global answer1
    global answer2
    global N
    if mat[i][j]!=0:
        i1=i
        j1=j
        while i1<N and j1<N:
            mat[i1][j1] = 0
            i1+=1
            j1+=1
        i2 = i
        j2 = j
        while i2<N and j2>=0:
            mat[i2][j2] = 0
            i2+=1
            j2-=1
        if (i*N+j)%2==0:
            answer1 = max(answer1,cnt+1)
        else:
            answer2 = max(answer2,cnt+1)
    # print(cnt)
    for b in range(i*N+j+2,N*N,2):
        k = b//N
        l = b%N
        if mat[k][l]!=0:
            mat_copy = copy.deepcopy(mat)
            dfs(mat_copy,k,l,cnt+1)
            
cnt=0
for a in range(0,N*N,2):
    i = a//N
    j = a%N
    if chess[i][j]!=0:
        chess_copy = copy.deepcopy(chess)
        dfs(chess_copy,i,j,cnt)
        # print(chess)
# print('-----------------------------------')
# print(chess)
for a in range(1,N*N,2):
    i = a//N
    j = a%N
    if chess[i][j]!=0:
        chess_copy = copy.deepcopy(chess)
        dfs(chess_copy,i,j,cnt)
        # print(chess)

print(answer1+answer2)
print(N)