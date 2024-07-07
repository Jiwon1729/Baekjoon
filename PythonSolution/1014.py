import sys
# import random
T = int(sys.stdin.readline())

def sit(Mat,r,c,cnt):
    global res
    if Mat[r][c]=='.':
        Mat[r][c-1], Mat[r][c+1], Mat[r][c],Mat[r-1][c-1],Mat[r-1][c+1],Mat[r+1][c-1],Mat[r+1][c+1] ='x', 'x', 'x', 'x', 'x', 'x' , 'x'
        cnt+=1
    if r!=1 or c!=1:
        if c!=1:
            sit(Mat,r,c-1,cnt)
        else:
            sit(Mat,r-1,C,cnt)
    else:
        res=max(cnt,res)
    return Mat

results=[]
for _ in range(T):
    R, C = map(int, sys.stdin.readline().split())
    Mat = [sys.stdin.readline().strip() for i in range(R)]
    sit_Mat=[['x' for i in range(C+2)]]
    for i in range(len(Mat)):
        temp = ['x']
        for j in range(len(Mat[i])):
            temp.append(list(Mat[i])[j])
        temp.append('x')
        sit_Mat.append(temp)
    temp2 = ['x' for i in range(C+2)]
    sit_Mat.append(temp2)
    cnt = 0
    res = 0
    # print(sit_Mat)
    sit(sit_Mat,R,C,cnt)
    results.append(res)

for result in results:
    sys.stdout.write(str(result)+'\n')
