s, N, K, R1, R2, C1, C2 = map(int,input().split())

def fractal(s,N,K,i,j):
    mid_st = (N**(s))*((N-K)//2)
    mid_ed = (N**(s))*(((N-K)//2)+K)
    if (i<mid_st or i>=mid_ed) or (j<mid_st or j>=mid_ed):
        if s==0:
            return 0
        else:
            return fractal(s-1,N,K,i%(N**(s)),j%(N**(s)))
    else:
        return 1
answer = []
if s==0:
    print(0)
else:
    for i in range(R1,R2+1):
        tmp2 = []
        for j in range(C1,C2+1):
            tmp = fractal(s-1,N,K,i,j)
            tmp2.append(tmp)
        answer.append(tmp2)
    for a in answer:
        print("".join(map(str,a)))