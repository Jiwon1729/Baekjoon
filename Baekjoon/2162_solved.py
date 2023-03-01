import sys

def CCW(x1,x2,x3,y1,y2,y3):
    if (x1*y2-x2*y1)*(x1*y3-x3*y1)<0:
        return 1
    elif (x1*y2-x2*y1)*(x1*y3-x3*y1)==0:
        return 0
    else:
        return -1
    
def find(x):
    if x!=parent[x]:
        x = find(parent[x])
    return x

def union(a,b):
    a = find(a)
    b = find(b)
    if a>b:
        parent[a] = b
    elif a<b:
        parent[b] = a

position =[]
N = int(sys.stdin.readline())
parent = [i for i in range(N)]

for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    position.append(line)

for i in range(N-1):
    for j in range(i+1,N):
        # print(i,j)
        if parent[i]!=parent[j]:
            x1 = position[i][2]-position[i][0]
            x2 = position[j][2]-position[i][0]
            x3 = position[j][0]-position[i][0]
            x4 = position[j][2]-position[j][0]
            x5 = position[i][2]-position[j][0]
            x6 = position[i][0]-position[j][0]
            y1 = position[i][3]-position[i][1]
            y2 = position[j][3]-position[i][1]
            y3 = position[j][1]-position[i][1]
            y4 = position[j][3]-position[j][1]
            y5 = position[i][3]-position[j][1]
            y6 = position[i][1]-position[j][1]
            a = CCW(x1,x2,x3,y1,y2,y3)
            b = CCW(x4,x5,x6,y4,y5,y6)
            c = CCW(x2,x3,x4,y2,y3,y4)
            d = CCW(x3,x4,x5,y3,y4,y5)
            # 한  점이 일치하는 경우
            if ((position[j][2]==position[i][2] and position[j][3]==position[i][3]) or
                (position[j][0]==position[i][2] and position[j][1]==position[i][3]) or
                (position[j][2]==position[i][0] and position[j][3]==position[i][1]) or
                (position[j][0]==position[i][0] and position[j][1]==position[i][1])):
                union(i,j)
            # 두 선분이 한 직선 위에 있을 경우
            elif a==0 and b==0 and c==0 and d ==0: 
                maxax, minax = max(position[i][2],position[i][0]), min(position[i][2],position[i][0])
                maxbx, minbx = max(position[j][2],position[j][0]), min(position[j][2],position[j][0])
                maxay, minay = max(position[i][3],position[i][1]), min(position[i][3],position[i][1])
                maxby, minby = max(position[j][3],position[j][1]), min(position[j][3],position[j][1])
                if (((maxax<=maxbx and maxax>=minbx) and (maxay<=maxby and maxay>=minby)) or
                    ((maxbx<=maxax and maxbx>=minax) and (maxby<=maxay and maxby>=minay))):
                    union(i,j)
                # elif c==1:
                #     union(i,j)
            #교차하는 경우
            elif a>=0 and b>=0: 
                union(i,j)
        parent[i]=find(i)
        parent[j]=find(j)
for i in range(len(parent)):
    parent[i] = find(i)
        # print(parent)
# 

# print(parent)
answer = len(set(parent))
tmp = list(set(parent))
answer2 = 0
for i in tmp:
    answer2=max(answer2,parent.count(i))
print(answer)
print(answer2)

