# 200213

import sys

N = int(sys.stdin.readline())
'''
마지막 숫자, 들어가 있는 숫자. 이전 값
'''
dp=[[[ 0 for i in range(1<<10)]  for _ in range(10)] for j in range(N)]
for i in range(1,10):
    dp[0][i][1<<i]=1
# print(dp)
for i in range(1,N):
    for j in range(10):
        for k in range(1<<10): # choose 0-9 number
            if j-1>=0:
                dp[i][j-1][k |(1<<(j-1))] += dp[i-1][j][k]
            if j+1<=9:
                dp[i][j+1][k | (1<<(j+1))] += dp[i-1][j][k]
    

answer = 0
for j in range(10):
    answer+=dp[N-1][j][(1<<10)-1]
answer= answer%1000000000
print(answer)
