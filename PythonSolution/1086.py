import math

N = int(input())
arr = []
div = 0
lenarr = []
for i in range(N):
    y = input()
    div+=len(y)
    lenarr.append(len(y))
    arr.append(int(y))
K = int(input())
arr2 = []
for i in range(N):
    arr3 = []
    a = arr[i]
    for j in range(div):
        a = a%K
        arr3.append(a)
        a = a*10
    arr2.append(arr3)
answer = 0
# print(arr2)
# print('---------------')
def permutation(digit,check,remain,cnt):
    global answer
    global K
    for i in range(N):
        if check&(1<<i)>0:
            if cnt == 0:
                # print(remain)
                if (remain+arr2[i][digit])%K == 0:
                    answer+=1
            else:
                # print("permutaion")
                permutation(digit+lenarr[i],check-(1<<i),remain+arr2[i][digit],cnt-1)

for i in range(N):
    permutation(lenarr[i],(1<<N)-1-(1<<i),arr2[i][0],N-2)
    # print("--------------------------")
def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return 1
# print(answer)
if answer ==0:
    print("0/1")
else:
    tmp4 =math.gcd(answer,factorial(N))
    print(str(answer//tmp4)+"/"+str(factorial(N)//tmp4))