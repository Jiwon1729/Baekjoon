N, L = map(int,input().split())
answer = [-1]
while L<=100:
    tmp = (2*N-L*(L-1))%(L*2)
    if tmp==0:
        a = int((2*N-L*(L-1))/(L*2))
        if a < 0:
            break
        else:
            answer = []
            for i in range(L):
                answer.append(a+i)
            break
    else:
        L+=1
print(" ".join(map(str,answer)))