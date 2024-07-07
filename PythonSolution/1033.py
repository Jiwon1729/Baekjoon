N = input()
answer = [1 for _ in range(N)]
cnt = [0 for _ in range(N)]
queue =[]
for i in range(N-1):
    a, b, p, q = map(int,input().split())
    cnt[a]+=1
    cnt[b]+=1
    tmp = [a,b,p,q]
    queue.append(tmp)

for s,e,sp,sq in queue:
    print(s,e,sp,sq)
while True:
    if min(cnt[a],cnt[b])==1:
        cnt[a]-=1
        cnt[b]-=1
        if answer[a]