N = int(input())
building = list(map(int,input().split()))
watch = [0 for _ in range(N)]
start_linear = -1e10
leftstart_linear = 1e10
answer=0
for i in range(N):
    cnt = 0
    if i!=N-1:
        right_linear = start_linear
        for j in range(i+1,N):
            new_linear = (building[j]-building[i])/(j-i)
            if right_linear<new_linear:
                cnt+=1
                right_linear=new_linear
    if i!=0:
        left_linear = leftstart_linear
        for j in range(i-1,-1,-1):
            new_linear = (building[i]-building[j])/(i-j)
            if left_linear>new_linear:
                cnt+=1
                left_linear=new_linear
    answer=max(cnt,answer)
print(answer)
