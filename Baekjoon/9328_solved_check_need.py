import sys
from collections import deque
def bfs(visited):
    global answer
    queue = deque([[0, 0]])
    # print(visited_doc)
    # print(visited)
    while queue:
        r, c = queue.popleft()
        for k in range(4):
            r2=r+dx[k]
            c2=c+dy[k]
            if c2 < 0 or c2 >= w + 2 or r2 < 0 or r2 >= h + 2 or maze[r2][c2]=='*' or visited[r2][c2]==True:
                continue
            # print(i2,j2)
            if 'A'<=maze[r2][c2]<='Z':
                if chr(ord(maze[r2][c2]) + 32) not in key:
                    continue
            elif 'a'<=maze[r2][c2]<='z' and maze[r2][c2] not in key:
                key[maze[r2][c2]] = True
                visited = [[False] * (w + 2) for _ in range(h + 2)]
            elif maze[r2][c2] =='$' and [r2,c2] not in visited_doc:
                answer+=1
                visited_doc.append([r2,c2])
            visited[r2][c2] = True
            queue.append([r2,c2])
T = int(sys.stdin.readline())
dx=[-1,0,0,1]
dy=[0,-1,1,0]
for _ in range(T):
    h, w =map(int,sys.stdin.readline().split())
    maze = []
    for _ in range(h):
        tmp =list('.'+str(sys.stdin.readline().strip('\n'))+'.')
        maze.append(tmp)
    maze = ['.' * (w + 2)] + maze + ['.' * (w + 2)]
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    key = {}
    visited_doc = []

    for i in sys.stdin.readline():
        if i.isalpha():  # 만약 알파벳이면
            key[i] = True  # 키로 저장
    # print(visited)
    answer = 0
    bfs(visited)
    print(answer)
# print("end")


