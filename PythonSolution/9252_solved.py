# 230215
import sys
N = str(sys.stdin.readline())
M = str(sys.stdin.readline())
l1 = len(N)
l2 = len(M)
ans_array = [[""]*(l2+1) for _ in range(l1+1)]
# print(ans_array)
for i in range(1,l1+1):
    for j in range(1,l2+1):
        if N[i-1]==M[j-1]:
            ans_array[i][j]=ans_array[i-1][j-1]+N[i-1]
        else:
            if len(ans_array[i][j-1])>len(ans_array[i-1][j]):
                ans_array[i][j] = ans_array[i][j-1]
            else:
                ans_array[i][j] = ans_array[i-1][j]
if len(ans_array[-1][-1])=="":
    print(0)
else:
    answer=ans_array[-1][-1].strip('\n')
    print(len(answer))
    print((answer))
# print(ans_array)

# answer = 0
# ans_str = ""
# for i in range(len(N)):
#     k=answer
#     for j in range(len(M)):
#         while N[i:i+k]==M[j:j+k] and i+k<len(N) and j+k<len(N):
#             if k>answer:
#                 ans_str=N[i:i+k]
#                 answer = k
#             k=k+1

# if answer == 0:
#     print(0)
# else:
#     [print(answer)]
#     print(ans_str)

