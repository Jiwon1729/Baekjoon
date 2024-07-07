import copy
import bisect
N = int(input())
A = list(map(int,input().split()))
A.sort()
B = copy.deepcopy(A)
C = [0 for i in range(N)]
answer = 0
if N<=2:
    print(0)
else:
    cnt_tmp = 0
    tmp2 =0
    for i in range(N):
        if B[i]==0:
            cnt_tmp+=1
            tmp2=i
        elif B[i]>0:
            break
    if cnt_tmp>2:
        answer+=cnt_tmp-1
        B=B[0:tmp2-cnt_tmp+1]+B[tmp2:]
    
    for i in range(N-1):
        for j in range(i+1,N):
            tmp = bisect.bisect_left(B, A[i]+A[j])
            # print(tmp,A[i]+A[j])
            while tmp<len(B):
                if B[tmp]==A[i]+A[j]:
                    if tmp!=i and tmp!=j:
                        C[tmp]=1
                    tmp+=1
                else:
                    break
            # print(k,i,j)
    # print(C)
    answer = sum(C)
    if cnt_tmp>2:
        answer+=cnt_tmp-1
    print(answer)

# n=int(input())
# arr=sorted(list(map(int, input().split())))
# answer=0
# for i in range(n):
#     tmp=arr[:i]+arr[i+1:]
#     l, r=0, len(tmp)-1
#     while l<r:
#         result=tmp[l]+tmp[r]
#         if result==arr[i]:
#             answer+=1
#             break
#         if result<arr[i]:
#             l+=1
#         else:
#             r-=1
# print(answer)