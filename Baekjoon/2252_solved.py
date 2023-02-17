# 230216

import sys
import heapq
# input
N, M = map(int,sys.stdin.readline().split())
order_list=[[] for _ in range(N+1)]
order_num = [0 for _ in range(N+1)]
queue=[]
for i in range(M):
    st, ed = map(int,sys.stdin.readline().split())
    order_list[st].append(ed)
    order_num[ed]+=1
# function
# print(order_list)
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

print(" ".join(map(str,answer)))