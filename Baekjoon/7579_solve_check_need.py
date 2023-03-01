import sys
N, M=map(int,sys.stdin.readline().split())

'''
M의 크기가 크다.
M 이상을 확보, cost 최대화 --> cost가 주어질 때 memory값이
M 이상이 되는 것중 M의 최댓값을 구하기
'''
memory = list(map(int,sys.stdin.readline().split()))
cost = list(map(int,sys.stdin.readline().split()))
cost_sum = sum(cost)+1
total_cost= [[0 for i in range(cost_sum)] for _ in range(N+1)]
answer = sum(cost)
# 2차원 행렬로 만드는 이유는 재귀적 용법을 쓸 떄 물건을 중복해서 더하지 않기 위해서이다
for i in range(N):
    for j in range(cost_sum):
        if j>=cost[i]:
            total_cost[i+1][j] = max(total_cost[i][j],total_cost[i][j-cost[i]]+memory[i])
        else:
            total_cost[i+1][j] = total_cost[i][j]
for i in range(cost_sum):
    if total_cost[N][i]>=M:
        answer=min(answer,i)
print(answer)        