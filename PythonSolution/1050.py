N, M = map(int,input().split())
pills = {}
pills['LOVE']=-1
for i in range(N):
    a, b = map(str,input().split())
    pills[a] = int(b)
pills2 = []
for i in range(M):
    a, b = map(str,input().split("="))
    if a not in pills:
        pills[a] = -1
    c = [[],[],a]
    tmp1 = ""
    tmp2 = ""
    for i in b:
        if i == "+":
            c[0].append(int(tmp1))
            c[1].append(tmp2)
            if tmp2 not in pills:
                pills[tmp2] = -1
            tmp1=""
            tmp2=""
        elif ord(i)>=48 and ord(i)<=57:
            tmp1+=i
        else:
            tmp2+=i
    c[0].append(int(tmp1))
    c[1].append(tmp2)
    if tmp2 not in pills:
        pills[tmp2] = -1
    pills2.append(c)
n = 0
# print(pills2)
while n<=M*2:
    n+=1
    for pill2 in pills2:
        price = 0
        tmp = []
        for k in pill2[1]:
            tmp.append(pills[k])
        if -1 not in tmp:
            for i in range(len(pill2[0])):
                price+=pill2[0][i]*tmp[i]
            if pills[pill2[2]]!=-1:
                pills[pill2[2]]=min(pills[pill2[2]],price)
            else:
                pills[pill2[2]]=price
if pills['LOVE']==-1:
    print(-1)
elif pills['LOVE']>1000000000:
    print(1000000001)
else:
    print(pills['LOVE'])