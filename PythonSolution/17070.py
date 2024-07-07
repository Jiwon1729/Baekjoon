N = int(input())
mat = []
for i in range(N):
    tmp = list(map(int,input().split()))
    mat.append(tmp)
answer = 0
def dfs(x,y,p):
    global answer
    if x==N-1 and y==N-1:
        answer+=1
    else:
        if x+1<N:
            if p!=0 and mat[x+1][y]==0:
                dfs(x+1,y,1)
        if y+1<N:        
            if p!=1 and mat[x][y+1]==0:
                dfs(x,y+1,0)
        if x+1<N and y+1<N:
            if mat[x][y+1]==0 and mat[x+1][y]==0 and mat[x+1][y+1]==0:
                dfs(x+1,y+1,2)
dfs(0,1,0)
print(answer)