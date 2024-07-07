import math
a, b = map(int,input().split(" "))
def era(b):
    n = int(((b**(1/2))//1)+2)
    # print(n)
    check = [True]*n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if check[i] == True:
            for j in range(i+i, n, i):
                check[j] = False
    # return check
    return [i**2 for i in range(2, n) if check[i] == True]
check = era(b)
# print(len(check))
answer = 0
check2 = []
for j in check:
    tmp = (a//j)*(j)
    if tmp<a:
        tmp+=j
    check2.append([tmp,j])
# print(check2)
check2.sort()
check3 = [True]*(b-a+1)
for ch in check2:
    # print(ch)
    for j in range(ch[0],b+1,ch[1]):
        check3[j-a] = False
# print(check3)
print(check3.count(True))
# print(check2)
# print(b-a+1-answer)

# st = int(((a**(1/2))//1)-2)
# arr =[]
# answer = 0
# # print(len(check))
# # print(st)
# for i in range(st,len(check)):
#     # print(i)
#     if i**2>=a and i**2<=b:
#         answer+=1
# # print(answer)
    
# 10000000000 10001000000
# 1 1000000