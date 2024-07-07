N = int(input())
ship = list(map(int,input().split()))
M = int(input())
box = list(map(int,input().split()))

box.sort(reverse=True)
ship.sort(reverse=True)
check=[0 for _ in range(M)]
cnt = 0
cnt2 = 0
answer = 0
if box[0]>ship[0]:
    cnt = -1
else:
    while cnt2<M:
        i=0
        j=0
        while i<N and j<M:
            # print(i,j,"ij")
            if check[j]==1:
                j+=1
            elif ship[i]>=box[j]:
                check[j]=1
                # print(i,j)
                i+=1
                j+=1
                cnt2+=1
            else:
                j+=1
            if i==N or j==M:
                cnt+=1
print(cnt)