import sys
sys.setrecursionlimit(10**5)
N = int(sys.stdin.readline())
def dfs(a):
    for i in range(len(parent[a])):
        if answer[parent[a][i]] == 0:
            answer[parent[a][i]] = a
            dfs(parent[a][i])
parent = [[] for i in range(N+1)]
for i in range(N-1):
    a, b =map(int,sys.stdin.readline().split())
    parent[b].append(a)
    parent[a].append(b)
# print(parent)
answer=[0 for i in range(N+1)]
answer[0] = 1
answer[1] = 1
tmp=[0,1]
dfs(1)
# print(answer)
for i in answer[2:]:
  print(i)