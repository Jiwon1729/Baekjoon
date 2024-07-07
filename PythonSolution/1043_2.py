import heapq
N, M =map(int,input().split())
know = list(map(int,input().split()))
know = set(know[1:])
parties = []

for i in range(M):
    tmp = list(map(int,input().split()))
    tmp = tmp[1:]
    parties.append(tmp)

Flag = [1 for _ in range(M+1)]
tmp = set()
while know:
    for i in range(len(parties)):
        if know | parties[i]:
            for j in parties[i]:
                tmp.add(j)
                Flag[i] = 0
    if know == tmp:
        break
    else:
        know = tmp
print(Flag)
answer = sum(Flag)-1
print(answer)
# def union(x,y):
#     x = find(x)
#     y = find(y)
#     parent[x] = y

# def find(x):
#     if parent[x]==x:
#         return x
#     else:
#         y=find(parent[x])
#         return y