X, K = map(int, input().split())

tmp = [0 for i in range(60)]
cnt = 0
Flag = 1
while X>0 or 0 in tmp:
    if X%2==0 or X==0:
        tmp[cnt] = Flag
        cnt+=1
    Flag*=2
    X=X//2
tmp2 = []
while K>0:
    tmp2.append(K%2)
    K=K//2
answer = 0
for i in range(len(tmp2)):
    answer+=tmp2[i]*tmp[i]
print(answer)