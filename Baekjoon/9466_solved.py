# 230216
import sys
import heapq
T =int(sys.stdin.readline())
# def find(x):
#     if x!=parent(x):
#         x = find(parent(x))
#     return x
# def union(a,b):
#     global answer
#     x = find(a)
#     y = find(b)
#     if x==y:
#         answer-=(cycle_cnt[a]+cycle_cnt[b]+1)
#     elif x != y: # cycle이 아닐 시
#         parent[max(x,y)] = min(x,y)
# answer_list = []
for _ in range(T):
    N = int(sys.stdin.readline())
    order_list=[[] for _ in range(N+1)]
    order_num = [0 for _ in range(N+1)]
    queue = []
    # print(order_list)
    tmp = list(map(int,sys.stdin.readline().split()))
    tmp = [0]+tmp
        # print(tmp)
    for i in range(len(tmp)):
        order_list[i].append(tmp[i])
        order_num[tmp[i]]+=1
    for i in range(1,N+1):
        if order_num[i] ==0:
            heapq.heappush(queue,i)        
    # print(order_list)
    # print(order_num)
    answer = 0
    # print(order_num)
    while queue:
        # print(queue)
        answer+=1
        a = heapq.heappop(queue)
        # print(a)
        for i in order_list[a]:
            order_num[i]=order_num[i]-1
            if order_num[i]==0:
                heapq.heappush(queue,i)
    print(answer)
    # N = int(sys.stdin.readline())
    # parent = [i for i in range(N+1)]
    # cycle_cnt=[0 for i in range(N+1)]
    # tmp = list(map(int,sys.stdin.readline().split()))
    # tmp = [0]+tmp
    # answer = N
    # for i in range(1,len(tmp)):
    #     union(i,tmp[i])
    

