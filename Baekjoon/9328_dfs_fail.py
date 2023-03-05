import sys
import copy
from collections import deque
sys.setrecursionlimit(10**7)
T = int(sys.stdin.readline())
def dfs(x,y):
    global answer
    queue = deque([[x, y]])
    while queue:
        i, j = queue.popleft()
        print(i,j)
        ch = 1
        if maze[i][j]=='*':
            ch = 0
        elif 'a'<=maze[i][j]<='z' and maze[i][j] not in keys:
            keys.append(maze[i][j])
        elif 'A'<=maze[i][j]<='Z':
            if maze[i][j].lower() not in keys:
                k = large.index(maze[i][j])
                if [i,j] not in will_go[k]:
                    will_go[k].append([i,j])
                ch = 0
        elif maze[i][j]=='$':
            answer+=1
        print(queue)
        if ch == 1: 
            maze[i][j]='*'
            for k in range(len(dx)):
                i2=i+dx[k]
                j2=j+dy[k]
                # print(i2,j2)
                if i2>=0 and i2<len(maze) and j2>=0 and j2<len(maze[0]) and maze[i2][j2]!='*':
                    queue.append([i2,j2])

for _ in range(T):
    h, w =map(int,sys.stdin.readline().split())
    dx=[-1,0,0,1]
    dy=[0,-1,1,0]
    maze = []
    for _ in range(h):
        tmp =list(str(sys.stdin.readline().strip('\n')))
        maze.append(tmp)
    # print(maze)
    keys=list(str(sys.stdin.readline().strip('\n')))
    key_copy =copy.deepcopy(keys)
    answer = 0
    will_go=[[]for i in range(27)]
    large = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'
             ,'P','Q','R','S','T','U','V','W','X','Y','Z']
    small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(h):
        for j in range(w):
            if j==0 or j==(w-1) or i==0 or i==(h-1):
                if maze[i][j]!='*':
                # print(i,j)
                    dfs(i,j)
                    # print(i,j)
    # print("maze")
    change = 1
    while key_copy!=keys:
        key_copy = copy.deepcopy(keys)
        i = 0
        while change == 1:
            print(maze)
            for i in range(len(keys)):
                key = small.index(keys[i])
                while will_go[key] !=[]:
                    # print(will_go)
                    dfs(will_go[key][0][0],will_go[key][0][1])
                    will_go[key].remove(will_go[key][0])
                    # print(will_go)
            if key_copy == keys:
                break

    print(answer)
# print("end")


