N = int(input())
P = list(map(int,input().split()))
M = int(input())

answer = 1
if N==0:
    answer = "0"
else:
    price_rev = list(reversed(P))
    min1 = min(price_rev)
    min_num = price_rev.index(min1)
    cnt = [0 for _ in range(N)]
    first_num = ''
    if min_num == N-1:
        tmp2 = M//min1
        M = M%min1
        while tmp2>=0:
            for i in range(N-1):
                if price_rev[i]<=M:
                    first_num = str(N-i-1)
                    M-=price_rev[i]
                    cnt[N-1] = tmp2
                    tmp2 = -1
                    break
            if tmp2!=-1:
                M+=min1
                tmp2-=1
        if first_num == "":
            answer = "0"
    else:
        cnt[min_num] = M//min1
        M = M%min1
    cnt2 = 1
    for i in range(N):
        if M>=price_rev[i]:
            cnt[i]+=1
            M-=price_rev[i]
            break
    while cnt2:
        cnt2 = 0
        for i in range(N):
            if M+min1>=price_rev[i] and min1!=price_rev[i] and cnt[min_num]>0 and min_num>i:
                cnt2 = 1
                cnt[min_num]-=1
                cnt[i]+=1
                M = M+min1-price_rev[i]
                break
    if answer!="0":
        answer = first_num
        for i in range(N):
            answer+=str(N-i-1)*cnt[i]
print(answer)