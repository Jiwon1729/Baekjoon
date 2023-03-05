#230220
import sys
import heapq
N = int(sys.stdin.readline())
a=-(10**10)
mem = [a for _ in range(N+1)]
A = [a] + list(map(int,sys.stdin.readline().split()))
B=[a]
D = [0]
k=0
max_val = 0
answer =[]
def bin_search(a):
    # print(B)
    start = -1
    end = len(B)
    while start+1<end:
        mid = (start+end)//2
        if B[mid]<a:
            start=mid
        elif B[mid]>a:
            end=mid
        else:
            return mid
    return end

for i in range(1,len(A)):
    j=len(B)-1
    if B[j]<A[i]:
        B.append(A[i])
        max_val+=1
        D.append(max_val)
    else:
        po = bin_search(A[i])
        B[po] = A[i]
        D.append(po)
print(max_val)
for i in range(len(A)-1,0,-1):
    # print(i,"i")
    # print(i,max_val)
    if D[i] == max_val:
        answer.append(A[i])
        max_val-=1
        if max_val ==0:
            break
answer.sort()
print(" ".join(map(str,answer)))
# # print(D)
# # print(A)
# # print(B)
# print(answer,"answer")
# mem[0] = arr_num[0]
# dir_value = 0
# answer =[arr_num[0]]
# for i in range(1,N):
#     k = arr_num[i]
#     # print(k,dir_value)
#     if mem[dir_value]<k:
#         dir_value += 1
#         mem[dir_value] = k
#         # heapq.heappush(answer,k)
#     else:
#         print(k)
#         j = dir_value
#         while j>=0:
#             if mem[j]>k:
#                 if j==0:
#                     mem[j] = k
#                 j-=1
#             else:
#                 mem[j+1] = k
#                 break
#     # print(mem)
# print(dir_value+1)
# answer =mem[0:dir_value+1]