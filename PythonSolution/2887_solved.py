import sys

def find(x):
    if x!=parent[x]:
        x = find(parent[x])
    return x

def union(a,b,c):
    global answer
    a = find(a)
    b = find(b)
    if a!=b:
        answer+=c
        if a>b:
            parent[a] = b
        else:
            parent[b] = a

N = int(sys.stdin.readline().strip("\n"))
parent = [i for i in range(N+1)]
answer = 0
axis = []

for i in range(N):
    x,y,z = map(int,sys.stdin.readline().split())
    tmp  = [i,x,y,z]
    axis.append(tmp)

axis.sort(key = lambda x: (x[1]))
value = []
for i in range(N-1):
    value.append([axis[i+1][0], axis[i][0], (axis[i+1][1]-axis[i][1])])
value.append([axis[N-1][0], axis[0][0], (axis[N-1][1]-axis[0][1])])

axis.sort(key = lambda x: (x[2]))
for i in range(N-1):
    value.append([axis[i+1][0], axis[i][0], axis[i+1][2]-axis[i][2]])
value.append([axis[N-1][0], axis[0][0], (axis[N-1][2]-axis[0][2])])

axis.sort(key = lambda x: (x[3]))
for i in range(N-1):
    value.append([axis[i+1][0], axis[i][0], axis[i+1][3]-axis[i][3]])
value.append([axis[N-1][0], axis[0][0], (axis[N-1][3]-axis[0][3])])

value.sort(key = lambda x: (x[2]))
# print(value)
for i in range(len(value)):
    union(value[i][0],value[i][1],value[i][2])
    # print(answer)

print(answer)
