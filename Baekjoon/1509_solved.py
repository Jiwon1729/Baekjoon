# 230213
import sys
word =str(sys.stdin.readline())
pel = [[] for _ in range(len(word))]

def ispelindrom(part,mid):
    it = min(len(part)-mid-1,mid)
    for i in range(it+1):
        # print(mid+i,mid-i,"odd")
        # print(part[mid+i],part[mid-i])
        if part[mid+i]==part[mid-i]:
            # print(start,end)
            pel[mid+i].append(mid-i)
        else:
            break
        
    it = min(len(part)-mid-1,mid-1)
    for i in range(it+1):
        if part[mid+i]==part[mid-i-1]:
            pel[mid+i].append(mid-i-1)
        else:
            break              

def solve(word):
    answer=[-1]
    for end in range(0,len(word)):
        ans = answer[end]+1
        for start in pel[end]:
            ans = min(answer[start]+1,ans)
        answer.append(ans)
    return answer[-1]
for mid in range(len(word)):
    ispelindrom(word,mid)
print(solve(word))
''' 펠린드롬 사용 시 dp를 이용하지 않은 경우(시간 초과)'''
# def solve(word):
#     answer = [-1]
#     for end in range(0,len(word)):
#         # print("-------------------",end)
#         ans = answer[end]+1
#         part = word[0:end]
#         start_num_set = []
#         for start in range(0,end):
#             # print(part,start,end)
#             pos_num = ispelindrom(part,start,end)
#             # print(pos_num)
#             if pos_num !=-1:
#                 start_num_set.append(pos_num)
#         for i in start_num_set:
#             # print(ans,i,answer)
#             # print(ans,answer[i+1],i,"answer,i")
#             ans=min(ans,(answer[i+1]+1))
#         # print(start_num_set,part,ans,answer)
#         answer.append(ans)
#     # print(answer)
#     return answer[-1]

# def ispelindrom(part,start,end):
#     for i in range((end-start)//2):
#         # print(part[start+i],part[end-1])
#         if part[start+i]!=part[end-i-1]:
#             return -1
# print(word)

    