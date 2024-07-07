T=int(input())
for i in range(T):
    a,b = map(int,input().split(" "))
    answer = 1
    tmp = 1
    cnt = 1
    while b>a:
        answer*=b
        tmp=tmp*cnt
        cnt+=1
        b-=1
    answer = answer//tmp
    print(answer)