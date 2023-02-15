# 230215
import sys
from copy import deepcopy
# input
N = int(sys.stdin.readline())
matrix =[]
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    matrix.append(tmp)

def mov_matrix(matrix,vector):
    if vector >1:
        matrix = [list(x) for x in zip(*matrix)]
    if vector%2 !=0:
        matrix2 = []
        for i in range(N):
            tmp = matrix[i]
            tmp.reverse()
            # print(tmp3)
            matrix2.append(tmp)
        matrix = matrix2
    for i in range(N):
        tmp = 0
        tmp2 = []
        for j in range(N):
            if tmp == 0:
                tmp = matrix[i][j]
            elif matrix[i][j]==0:
                continue
            elif matrix[i][j] == tmp:
                tmp=tmp*2
                tmp2.append(tmp)
                tmp = 0
            else:
                tmp2.append(tmp)
                tmp = matrix[i][j]
        if tmp!= 0:
            tmp2.append(tmp)
        while len(tmp2)!=N:
            tmp2.append(0)
        matrix[i] = tmp2
    return matrix

answer = 0
# def main(cnt,vector,matrix):
#     print(matrix,vector)
#     global answer
#     if cnt ==0:
#         for v in range(4):
#             main(cnt+1,v,mov_matrix(ch_mat(v,matrix)))
#     else:
#         # print(matrix)
#         if cnt == 1:
#             print(matrix,vector)
#             max_value = 0
#             for i in matrix:
#                 max_value = max(max(i),max_value)
#             answer = max(answer,max_value)
#         else:
#             for v in range(4):
#                 main(cnt+1,v,ch_mat(v,matrix))

def dfs(board, cnt):
    global answer
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                answer = max(answer, board[i][j])
        return

    for i in range(4):
        # if cnt ==4:
        #     print(board)
        tmp_board = mov_matrix(deepcopy(board), i)
        # print(tmp_board,i)
        dfs(tmp_board, cnt + 1)

if  N ==1:
    print(int(max(matrix[0])))
else:
    dfs(matrix,0)
    # print(matrix)
    print(answer)