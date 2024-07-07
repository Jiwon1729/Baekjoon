import copy
N = int(input())
cnt = [0 for i in range(10001)]
ar = list(map(int,input().split()))
for i in ar:
    cnt[i]+=1
ar = set(ar)
ar = list(ar)
ar.sort()
new_ar = copy.deepcopy(ar)
st = 0
if len(ar)==1:
    answer=cnt[i]*str(ar[0])
else:
    while st<len(ar):
        if ar[st]+1==ar[st+1]:
            if st+1 != len(ar)-1:
                tmp = ar[st+2]
                ar[st+2]=ar[st+1]
                ar[st+1]=tmp
            else:
                tmp = ar[st+1]
                ar[st+1]=ar[st]
                ar[st]=tmp
        st+=1
        if st+1>=len(ar)-1:
            break
    answer = ""
    for i in ar:
        answer+=cnt[i]*str(i)
print((" ").join(answer))