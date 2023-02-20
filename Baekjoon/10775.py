import sys
G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
parents = [i for i in range(G+1)]
def find(x):
    if x == parents[x]:
        return x
    else:
        y = find(parents[x])
        parents[x] = y
        return y

def union(x, y):
    global endgame
    x = find(x)
    y = find(y)
    if x != y: # cycle이 아닐 시
        parents[max(x,y)] = min(x,y)
cnt = 0
airplane=[]
for i in range(P):
    a = int(sys.stdin.readline())
    airplane.append(a)
for a in airplane:
    if find(a)!=0:
        cnt+=1
        union(a,find(a)-1)
    else:
        break
print(cnt)