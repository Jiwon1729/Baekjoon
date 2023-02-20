#230217~230220

import sys
tmp =  list(map(int,sys.stdin.readline().split()))
def ad_value(a,b):
    # print(a,b)
    if a==0 or  b==0:
        return 2
    elif a==b:
        return 1
    elif abs(a-b)==2:
        return 4
    else:
        return 3
if len(tmp) ==1:
    answer = 0
# elif len(tmp)==2:
#     answer = 2
else:
    a =10**7
    foot = [[[a for i in range(5)] for j in range(5)] for k in range(len(tmp))]
    # print(foot)
    for i in range(5):
        for j in range(5):
            foot[0][0][0]=0
    # print(foot)
    for k in range(len(tmp)-1):
        # print(tmp[k])
        for i in range(5):
            for j in range(5):
                if foot[k][i][j]!=a:
                    foot[k+1][tmp[k]][j]=min(foot[k+1][tmp[k]][j],foot[k][i][j]+ad_value(tmp[k],i))
                    # print(foot[k+1][tmp[k]][j],tmp[k],i)
                    foot[k+1][i][tmp[k]]=min(foot[k+1][i][tmp[k]],foot[k][i][j]+ad_value(tmp[k],j))
        # print(foot[k+1])
        # print(foot[1])
    # print(foot[1])
    # print(foot[0])
    answer = min(foot[len(tmp)-1][tmp[-2]])
    # print(foot[2])
    # print(foot[3])
    # print(foot[4])
    # print(tmp[-2])
    # answer = (foot[len(tmp)-1])
    # print(tmp[-2])
print(answer)
# k=0
# DDR=[tmp[0]]
# def dp(foot1,foot2,newfoot1,v1,v2):
#     a = ad_value(newfoot1,foot1[1])
#     b = ad_value(newfoot1,foot1[0])
#     if a<=b:
#         foot1 = [newfoot1,foot1[0]]
#         foot2 = [newfoot1,foot1[1]]
#         v1 = v1+a
#         v2 = v1+b
#     else:
#         foot2 = [newfoot1,foot1[0]]
#         foot1 = [newfoot1,foot1[1]]
#         v2 = v1+a
#         v1 = v1+b
#     if ad_value(newfoot1,foot2[1]) <= ad_value(newfoot1,foot2[0]):
#         foot3 = [newfoot1,foot2[0]]
#         v3 = v2 + ad_value(newfoot1,foot2[1])
#     else:
#         foot3 = [newfoot1,foot2[1]]
#         v3 = v2 + ad_value(newfoot1,foot2[0])
#     if v3<v2:
#         v2 = v3
#         foot2 = foot3
#     return foot1, foot2,v1, v2

# if len(tmp) ==1:
#     answer = 0
# for i in range(len(tmp)-1):
#     if tmp[i]==tmp[i+1]:
#         k+=1
#     else:
#         DDR.append(tmp[i+1])
        
# if len(DDR)==2:
#     answer=k+2
# elif len(DDR)==3:
#     answer=k+4
# else:
#     foot1 = [DDR[0],DDR[1]]
#     foot2 = [DDR[1],0]
#     v1 = 4+k
#     v2 = 2+ad_value(DDR[1],DDR[0])+k
#     # 이전거 1개, 
#     i=2
#     while DDR[i]!=0:
#         # print( foot1, foot2,v1, v2)
#         foot1, foot2,v1,v2 = dp(foot1,foot2,DDR[i],v1,v2)
#         i+=1
# print(v1)
