230225

import sys

D = int(sys.stdin.readline())
MOD = 1000000007
SIZE = 8

def multiply_matrix(matrix1, matrix2):
    return [[sum(matrix1[i][k]*matrix2[k][j] % MOD for k in range(SIZE)) % MOD
             for j in range(SIZE)] for i in range(SIZE)]

def solution(D):
    matrix1 = [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0]
    ]
    matrix =[]
    matrix.append(matrix1)
    need =[]
    while D!=0:
        a = D%2
        need.append(a)
        D = D//2
        if D==1:
            need.append(D)
            D=0
    for i in range(len(need)):
        tmp = multiply_matrix(matrix[i],matrix[i])
        matrix.append(tmp)
    cnt = 0
    for i in range(len(need)):
        if need[i]==1:
            if cnt==0:
                ans_mat =matrix[i]
                cnt = 1
            else:
                ans_mat = multiply_matrix(ans_mat,matrix[i])
    return ans_mat[0][0]

print(solution(D))