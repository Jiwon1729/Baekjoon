import copy
from collections import deque
N,M,V = map(int,input().split())

answer_dfs=[V]
answer_bfs=[V]
def dfs(start):
    # tmp2=[]
    for i in node[start]:
        if i not in answer_dfs:
            answer_dfs.append(i)
            # tmp2.append(i)
            dfs(i)
node = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)
for i in range(len(node)):
    node[i]=sorted(node[i])
node2 = copy.deepcopy(node)
queue = deque([])
queue.append(V)

dfs(V)
while queue:
    st = queue.popleft()
    tmp = []
    for i in node2[st]:
        if i not in answer_bfs:
            answer_bfs.append(i)
            queue.append(i)
            tmp.append(i)
    for i in tmp:
        node2[st].remove(i)

for i in range(len(answer_dfs)):
    answer_dfs[i]=str(answer_dfs[i])
for i in range(len(answer_bfs)):
    answer_bfs[i]=str(answer_bfs[i])
print(' '.join(answer_dfs))
print(' '.join(answer_bfs))