import sys
n = int(sys.stdin.readline())
'''
fib=[]
fib[2k]=fib[n-1]+fib[n-2]
=fib(k+1)*fib[k]+fib(k)*fib[k-1]
f(2k+1)
=fib(k+2)*fib(k+1)+fib(k+1)*fib(k)
0 
1 1 2 3 
5 8 13 21(678-->14,15,16-->30,31,32)
34
x 377 610 987
1597
'''
# fib_value=[0,1]
# k=2
# while k<10000:
#     tmp=(fib_value[k-1]+fib_value[k-2])%1000000007
#     fib_value[k]=tmp
#     k+=1
# def fib(n):
#     global k
#     global fib_value
#     if fib_value[n]!=None:
#         return fib_value[n]
#     else:
#         if (n%2)==0:
#             return (fib(n//2+1)+fib(n//2-1))*fib(n//2)
#         else:
#             return fib(n//2+1)**2+fib(n//2)**2
#             return fib(n//2+2)*fib(n//2)+fib(n//2+1)*fib(n//2-1)
ans=[[1,0],[0,1]]
F_m =[[1,1],[1,0]]
def mul(A,B):
    ans=[[0 for i in range(len(A))] for k in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B[0])):
                ans[i][k] =(ans[i][k]+A[i][j]*B[j][k])%1000000007
    return ans
mul_matrix=[F_m]
mul_num = []
while n>0:
    mul_num.append(n%2)
    n=n//2
for i in range(len(mul_num)):
    tmp = mul(F_m,F_m)
    mul_matrix.append(tmp)
    F_m = tmp
for i in range(len(mul_num)):
    if mul_num[i]==1:
        ans=mul(ans,mul_matrix[i])
        # print(ans)
answer = ans[1][0]
# print(mul_num)
# print(mul_matrix)
print(answer)