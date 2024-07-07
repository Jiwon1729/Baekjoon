import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, M, W = map(int, sys.stdin.readline().split())
    INF = 10**9
    # distance = [[[INF for _ in range(N)] for _ in range(N)] for _ in range(N)]
    distance = [[INF for _ in range(N)] for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         if i==j:
    #             distance[i][j]=0
    answer = "NO"
    road =[]
    for _ in range(M):
        s,e,t= map(int,sys.stdin.readline().split())
        tmp=[s-1,e-1,t]
        tmp2=[e-1,s-1,t]
        # road.append(tmp)
        # road.append(tmp2)
        distance[s-1][e-1]=min(t,distance[s-1][e-1])
        distance[e-1][s-1]=min(t,distance[e-1][s-1])
        # distance[s-1][e-1]=min(t,distance[s-1][e-1])
    for _ in range(W):
        s,e,t= map(int,sys.stdin.readline().split())
        tmp=[s-1,e-1,-t]
        if s == e :
            answer = "YES"
        # road.append(tmp)
        distance[s-1][e-1]=min(-t,distance[s-1][e-1])
        # distance[0][s-1][e-1]=min(-t,distance[0][s-1][e-1])
    for i in range(N):
        for j in range(N):
            if distance[i][j]!=INF:
                tmp = [i,j,distance[i][j]]
                road.append(tmp)
                
    # N개의 선을 연결
    di = [INF for _ in range(N)]
    for i in range(N):
        # 모든 node에 대하여
        for j in range(len(road)):
            st = road[j][0]
            ed = road[j][1]
            dist = road[j][2]
                # k에서 시작점까지의 길이 있고, 시작점을 들리고 ed로 가는 것이 k에서 ed로 가는 것보다 작다면
            if di[ed]>di[st]+dist:
                di[ed] = di[st]+dist
                if i==N-1:
                    answer="YES"
                    break
    # print(distance)
    print(answer)

# import sys
# T = int(sys.stdin.readline())
# for _ in range(T):
#     N, M, W = map(int, sys.stdin.readline().split())
#     INF = 10**9
#     # distance = [[[INF for _ in range(N)] for _ in range(N)] for _ in range(N)]
#     distance = [[[INF for _ in range(N)] for _ in range(N)] for _ in range(N+2)]
#     # for i in range(N):
#     #     for j in range(N):
#     #         if i==j:
#     #             distance[i][j]=0
#     answer = "NO"
#     road =[]
#     for _ in range(M):
#         s,e,t= map(int,sys.stdin.readline().split())
#         tmp=[s-1,e-1,t]
#         tmp2=[e-1,s-1,t]
#         # road.append(tmp)
#         # road.append(tmp2)
#         distance[0][s-1][e-1]=min(t,distance[0][s-1][e-1])
#         distance[0][e-1][s-1]=min(t,distance[0][e-1][s-1])
#         # distance[s-1][e-1]=min(t,distance[s-1][e-1])
#     for _ in range(W):
#         s,e,t= map(int,sys.stdin.readline().split())
#         tmp=[s-1,e-1,-t]
#         if s == e :
#             answer = "YES"
#         # road.append(tmp)
#         distance[0][s-1][e-1]=min(-t,distance[0][s-1][e-1])
#         # distance[0][s-1][e-1]=min(-t,distance[0][s-1][e-1])
#     for i in range(N):
#         for j in range(N):
#             if distance[0][i][j]!=INF:
#                 tmp = [i,j,distance[0][i][j]]
#                 road.append(tmp)

#     # N개의 선을 연결
#     for i in range(N+1):
#         # 모든 node에 대하여
#         for j in range(len(road)):
#             st = road[j][0]
#             ed = road[j][1]
#             dist = road[j][2]
#             for k in range(N):
#                 # k에서 시작점까지의 길이 있고, 시작점을 들리고 ed로 가는 것이 k에서 ed로 가는 것보다 작다면
#                 if distance[i][k][st]!=INF and distance[i][k][ed]>distance[i][k][st]+dist:
#                     distance[i+1][k][ed] = distance[i][k][st]+dist
#                 else:
#                     distance[i+1][k][ed] = distance[i][k][ed]
#                     # if i==N:
#                     #     answer="YES"
#                     #     break
#     for i in range(N):
#         for j in range(N):
#             if i==j and distance[N+1][i][j]<0:
#                 answer = "YES"
#     # print(distance)
#     print(answer)

#     # for i in range(1,N):
#     #     for j in range(N):
#     #         for k in range(N):
#     #             tmp=INF
#     #             for l in range(N):
#     #                 tmp = min(tmp,(distance[i-1][j][l]+distance[0][l][k]))
#     #             # tmp = min(distance[i-1][j][l]+distance[i-1][l][k] for l in range(N))
#     #             distance[i][j][k]=min(distance[i-1][j][k],tmp)
#     #             if j==k and distance[i][j][k]<0:
#     #                 answer = "YES"
#     #                 break
#     #         if answer == "YES":
#     #             break
#     #     if answer == "YES":
#     #         break
#         # print(distance[i])