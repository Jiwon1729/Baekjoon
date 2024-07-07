N =int(input())
answer = 0
def n_queen(N,now):
    global answer
    if now == N:
        # print(col)
        answer+=1
    else:
        for i in range(N):
            col[now] = i
            if promising(now):
                n_queen(N, now+1)
def promising(i):
    for j in range(0,i):
        if col[i]==col[j] or col[i]-col[j]==i-j or col[i]-col[j]==j-i:
            return False
    return True

# checknode
def n_queen2(N,now):
    global answer
    if promising2(now):
        if now == N:
            answer+=1
            print(col[1:])
        else:
            for j in range(1,N+1):
                col[now+1]=j
                n_queen2(N,now+1)
def promising2(i):
    for j in range(1,i):
        if col[i]==col[j] or col[i]-col[j]==i-j or col[i]-col[j]==j-i:
            return False
    return True

# expand
# def n_queen3(N,now):
#     global answer
#     for i in range(1,N+1):
#         col[now] = i
#         if promising2(now):
#             if now==N:
#                 print(col[1:])
#                 answer+=1
#             else:
#                 n_queen3(N, now+1)
# def promising2(i):
#     for j in range(1,i):
#         if col[i]==col[j] or col[i]-col[j]==i-j or col[i]-col[j]==j-i:
#             return False
#     return True

# improvement
def n_queen4(N,now):
    global answer
    for i in range(1,N+1):
        col[now] = i
        if promising3(now):
            if now==N:
                print(col[1:])
                answer+=1
            else:
                n_queen3(N, now+1)

answer = 0
col = [0 for _ in range(N+1)]
# n_queen2(N,0)
n_queen3(N,1)
print(answer)