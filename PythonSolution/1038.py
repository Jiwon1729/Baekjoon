from math import comb
N = int(input())
cnt = -1
tmp = cnt
k = 0
answer = 0
while True:
    cnt += comb(10,k)
    k+=1
    if cnt>=N:
        N=N-tmp
        break
    elif k>11:
        answer = -1
        break
    tmp = cnt
    print(tmp,cnt,N)

# arr = '9876543210'
# # arr2 = '123'
# # print(arr+arr2)
# num_array = []
# def combination(now,remain,count):
#     for i in range(len(remain)):
#         tmp = remain[i+1:]
#         choose = remain[i]
#         # print(now,remain,choose)
#         if count !=0 and tmp!='':
#             combination(now+choose,tmp,count-1)
#         elif count ==0:
#             tp = now+choose
#             tp = int(tp)
#             num_array.append(tp)
# # print(N-1)
# # N-=1
# # print(tmp)
# if answer !=-1:
#     k-=1
#     # for i in range(10):
#         # combination(i,0,arr,10,k)
#     combination('',arr,k-1)
#     num_array.sort()
#     if num_array!=[]:
#         answer=num_array[N]
# # print(str(arr))
# print(len(num_array))
# print(num_array)
# print(answer)
