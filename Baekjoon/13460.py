import sys
R, C = map(int,sys.stdin.readline().split())
rec = []
for _ in range(R):
    tmp=sys.stdin.readline().strip('\n')
    rec.append(tmp)
# print(rec)
for i in range(R):
    for j in range(C):
        if rec[i][j]=="R":
            r =[i,j]
        if rec[i][j]=="B":
            b =[i,j]
dx =[-1,0,0,1]
dy =[0,1,-1,0]
answer=[11]
def move(r,b,cnt):
    if cnt>10 or min(answer)<=cnt: # min(answer) 없어도 됨
        return 0
    for i in range(4):
        # print(i)
        k=0
        l=0
        ball=0
        ball2=0
        # print(rec[r[0]+(k+1)*dx[i]][r[1]+(k+1)*dy[i]])
        while rec[r[0]+(k+1)*dx[i]][r[1]+(k+1)*dy[i]]!="#":
            if rec[r[0]+(k+1)*dx[i]][r[1]+(k+1)*dy[i]]=="O":
                # print(1)
                ball = 1
            k+=1
        while rec[b[0]+(l+1)*dx[i]][b[1]+(l+1)*dy[i]]!="#":
            if rec[b[0]+(l+1)*dx[i]][b[1]+(l+1)*dy[i]]=="O":
                ball2 =1
            l+=1
        if (k==0 and l==0) or ball2==1:
            move(r,b,11)
        elif ball ==1:
            # print(l,k,r,b)
            answer.append(cnt)
        else:
            # if cnt<3:
                # print(cnt)
        # if cnt<3:
        #     print(r,b,cnt)
            if [r[0]+(k)*dx[i],r[1]+(k)*dy[i]]==[b[0]+(l)*dx[i],b[1]+(l)*dy[i]]:
                    if k>l:
                        k-=1
                        # if cnt<4:
                        #     print(r,b,i,cnt)
                    else:
                        l-=1
            # print("in",cnt,r,answer)
            move([r[0]+(k)*dx[i],r[1]+(k)*dy[i]],[b[0]+(l)*dx[i],b[1]+(l)*dy[i]], cnt+1)
move(r,b,1)
# print(answer)
if min(answer)==11:
    print(-1)
else:
    print(min(answer))