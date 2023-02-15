# 230215
import sys
sys.setrecursionlimit(10**7)
# input
N, M = map(int, sys.stdin.readline().split())
reps = [i for i in range(N+1)]

# 각 집합의 대표노드를 찾는 함수
def find(n):
    if reps[n] != n:
        reps[n] = find(reps[n])
    return reps[n]

# 두 개의 집합을 합치는 함수
def union(node1, node2):
    while node1 != reps[node1]:
        node1 = reps[node1]
    while node2 != reps[node2]:
        node2 = reps[node2]
    # rep3 = [find(node1),find(node2)]
    # rep1 = max(rep3)
    # rep2 = min(rep3)
    if node1 != node2:
        reps[max(node1,node2)] = min(node1,node2)
        return 0
    else:
        return 1
cnt = 0
answer = 0
mat =[]
for  _ in range(M):
    tmp = list(map(int, sys.stdin.readline().split()))
    mat.append(tmp)

for i in range(M):
    answer+=1
    cnt = union(mat[i][0], mat[i][1])
    if cnt==1:
        break
    # print(reps)
if cnt ==1:
    print(answer)
else:
    print(0)