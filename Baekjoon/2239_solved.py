import sys
import copy

board= []
for i in range(9):
    tmp = []
    tmp3 = sys.stdin.readline().strip('\n')
    for j in tmp3:
        tmp2 = int(j)
        # print(tmp2)
        tmp.append(tmp2)
    board.append(tmp)

# print(board)
C = 0
answer=[]

def dfs(x,y,board):
    global C
    global answer
    if C==1:
        exit
    elif board[x][y]!=0:
        if x==8 and y==8:
            board_copy=copy.deepcopy(board)
            answer=board_copy
            C=1
        elif y!=8:
            dfs(x,y+1,board)
        elif x!=8:
            dfs(x+1,0,board)
    else:
        tmp=set([1,2,3,4,5,6,7,8,9])
        i2=(x//3)*3
        j2=(y//3)*3
        A=set()
        for i in range(3):
            for j in range(3):
                A.add(board[i+i2][j+j2])
        for i in range(9):
            A.add(board[i][y])
            A.add(board[x][i])
        pos = list(tmp-A)
        if pos!=[]:
            pos.sort()
        # print(pos)
        for i in pos:
            board[x][y] = i
            if x==8 and y==8:
                C = 1
                board_copy=copy.deepcopy(board)
                answer = board_copy
            elif y!=8:
                dfs(x,y+1,board)
                board[x][y] = 0
            else:
                dfs(x+1,0,board)
                board[x][y] = 0
    
dfs(0,0,board)
for i in range(9):
    print("".join(map(str,answer[i])))
