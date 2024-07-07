N =int(input())
answer = 0
def n_queen(N,now):
    global answer
    if promising(now):
        if now==N-1:
            answer+=1
            print(col)
        else:
            for j in range(N):
                col[now+1]=j+1
                n_queen(N,now+1)
    # if now == N:
    #     check = 1
    #     print(col)
    #     return col
    # else:
    #     for i in range(N):
    #         col[now] = i+1
    #         if promising(now) and check == 0:
    #             n_queen(N, now+1)
def promising(i):
    for j in range(0,i):
        if col[i]==col[j] or col[i]-col[j]==i-j or col[i]-col[j]==j-i:
            return False
    return True
col = [1 for i in range(N)]
n_queen(N,0)
print(answer)