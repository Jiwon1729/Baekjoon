N, M = map(int,input().split())

mat =[]
for i in range(N):
    tmp = list(input())
    mat.append(tmp)
check_fun = [[] for _ in range(N)]
check_fun_2 = [0 for _ in range(M+1)]
K = int(input())
for i in range(N):
    tmp = []
    cnt = 0
    for j in range(M):
        if mat[i][j]=="0":
            tmp.append(j)
            cnt+=1
    tmp2 = [cnt,tmp]
    check_fun[i] = tmp2
    if cnt ==0:
        check_fun_2[0]+=1

print(check_fun)

for i in range(N):
    cnt = 0
    for j in range(i,N):
        # print(i,j)
        if check_fun[i]==check_fun[j]:
            cnt+=1
    check_fun_2[check_fun[i][0]] = max(check_fun_2[check_fun[i][0]], cnt)
answer = 0
for i in range(M+1):
    if i%2==K%2 and i<=K:
        answer = max(answer, check_fun_2[i])

print(answer)