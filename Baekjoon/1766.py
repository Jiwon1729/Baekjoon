import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph=[[] for i in range(N+1)]
in_Degree = [0 for _ in range(N+1)]
queue=[]
answer = []
# print(check_list)
for i in range(M):
    A, B = map(int,sys.stdin.readline().split())
    graph[A].append(B)
    in_Degree[B] +=1
in_Degree[0]=10000
for i in range(N+1):
    if in_Degree[i] == 0 :
        heapq.heappush(queue, i)
while queue:
    tmp = heapq.heappop(queue)
    answer.append(tmp)
    for i in graph[tmp]:
        in_Degree[i]-=1
        if in_Degree[i]==0:
            heapq.heappush(queue,i)

print(" ".join(map(str,answer)))
    # print(A,B)

# def find_prob(i):
#     for j in pr_list[i]:
#         if check_list[j] == True:
#             find_prob(j)
#     if check_list[i] == True:
#         answer.append(i)
#     check_list[i] = False
#     # print(pr_list)
#     # temp = set(pr_list[i])-set(answer)-set([0])
#     # if  temp == set() and check_list[i]==True:
#     #     check_list[i] = False
#     #     answer.append(i)
#     # else:
#     #     for j in temp:
#     #         if check_list[j] == True:
#     #             find_prob(j) 


# N, M = map(int, sys.stdin.readline().split())
# pr_list=[[0] for i in range(N+1)]
# check_list=[True] * (N+1)
# check_list[0] = False
# # print(check_list)
# for i in range(M):
#     A, B = map(int,sys.stdin.readline().split())
#     # print(A,B)
#     pr_list[B].append(A)
# for i in range(len(pr_list)):
#     temp=pr_list[i]
#     pr_list[i] = sorted(temp)
# print(pr_list)
# answer = []
# for i in range(1,N+1):
#     if check_list[i] == True:
#         find_prob(i)
# print(*answer,sep = ' ')