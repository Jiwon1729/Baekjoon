# 230216
import sys
T =int(sys.stdin.readline())
n =int(sys.stdin.readline())
A =list(map(int,sys.stdin.readline().split()))
m =int(sys.stdin.readline())
B =list(map(int,sys.stdin.readline().split()))
sumA = []
sumB = []
answer = 0
for i in range(n):
    tmp=0
    for j in range(i,n):
        tmp+=A[j]
        sumA.append(tmp)
for i in range(m):
    tmp=0
    for j in range(i,m):
        tmp+=B[j]
        sumB.append(tmp)
sumA.sort()
sumB.sort(reverse = True)
i = 0
j = 0
n = len(sumA)
m = len(sumB)
# print(sumA,sumB)
while i<n and j<m:
    # print(1)
    i2=1
    j2=1
    # print("check",i,j)
    while i2+i<n and sumA[i]==sumA[i+i2]:
        i2+=1
    while j2+j<m and sumB[j]==sumB[j+j2]:
        j2+=1
    if T>sumA[i]+sumB[j]:
        i+=1
    elif T<sumA[i]+sumB[j]:
        j+=1
    else:
        # print(i2,j2)
        answer+=i2*j2
        i=i+i2
        j=j+j2
print(answer)