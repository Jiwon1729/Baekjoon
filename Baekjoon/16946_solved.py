#230216
import sys
sys.setrecursionlimit(10**7)
N, M = map(int,sys.stdin.readline().split())
graph = []
for _ in range(N):
    tmp=list(map(str,sys.stdin.readline().strip('\n')))
    graph.append(tmp)
dx = [-1,0,0,1]
dy = [0,1,-1,0]

def dfs(x,y,cnt):
    global N
    global M
    global counting
    counting+=1
    graph[x][y] = cnt
    for i in range(4):
        if x+dx[i]>=0 and x+dx[i]<N and y+dy[i]<M and y+dy[i]>=0:
            if graph[x+dx[i]][y+dy[i]] == '0':
                dfs(x+dx[i],y+dy[i],cnt)

cnt = 1
counting_check=[0,0]
for i in range(N):
    for j in range(M):
        if graph[i][j]=='0':
            cnt+=1
            counting = 0
            dfs(i,j,cnt)
            counting_check.append(counting)
# print(counting_check)
# print(graph)
answer=[]
for x in range(N):
    tmp=[]
    for y in range(M):
        if graph[x][y]=='1':
            tmp2 = 0
            tmp3 =[]
            for i in range(4):
                if x+dx[i]>=0 and x+dx[i]<N and y+dy[i]<M and y+dy[i]>=0:
                    tmp4 = int(graph[x+dx[i]][y+dy[i]])
                    if tmp4 not in tmp3:
                        tmp3.append(tmp4)
            for i in tmp3:
                tmp2 = tmp2 + counting_check[i]
            tmp2+=1
            tmp2=tmp2%10
            tmp.append(tmp2)

        else:
            tmp.append(0)
    answer.append(tmp)
for i in range(len(answer)):
    print("".join(map(str,answer[i])))