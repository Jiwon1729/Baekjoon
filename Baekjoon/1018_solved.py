import sys

N, M =map(int, sys.stdin.readline().split())
chess =[]
answer = 0
for i in range(N):
    tmp=list(map(str,sys.stdin.readline().strip('\n')))
    chess.append(tmp)
sti=0
stj=0
ans = 2500
# print(N,M)
while sti+8<=N and stj+8<=M:
    # print(sti,stj)
    answer = 0
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                if chess[i+sti][j+stj]!='W':
                    answer+=1
                    # print(answer,i,j,'W')
            else:
                if chess[i+sti][j+stj]=='W':   
                    answer+=1
                    # print(answer,i,j)
    answer = min(answer,64-answer)
    # print(answer)
    ans=min(ans,answer)
    if (sti+8)<N:
        sti+=1
    elif (sti+8)==N:
        if (stj+8)<M:
            stj+=1
            sti=0
            # print(sti,stj)
        else:
            break
print(ans)