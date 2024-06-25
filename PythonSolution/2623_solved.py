# 230216

import sys
import heapq

N, M =map(int, sys.stdin.readline().split())
order_list=[[] for _ in range(N+1)]
order_num = [0 for _ in range(N+1)]
for _ in range(M):
    tmp = list(map(int,sys.stdin.readline().split()))
    tmp = tmp[1:]
    # print(tmp)
    for i in range(len(tmp)-1):
        order_list[tmp[i]].append(tmp[i+1])
        order_num[tmp[i+1]]+=1
# print(order_list)
# print(order_num)
queue = []
for i in range(1,len(order_list)):
    if order_num[i]==0:
        heapq.heappush(queue,i)
answer = []
while queue:
    a = heapq.heappop(queue)
    answer.append(a)
    for i in order_list[a]:
        order_num[i]-=1
        if order_num[i]==0:
            heapq.heappush(queue,i)
if len(answer) != N:
    print(0)
else:
    print(" ".join(map(str,answer)))