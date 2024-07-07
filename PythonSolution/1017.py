import math
import copy
#소수 리스트 만들기
def isPrime(val):
  return primes[val]
def bimatch(x):                                           
    if visited[x]:                                        
        return False                                      
    visited[x] = True                                     
                                                          
    for num in graph[x]:                                   
        if selected[num] == -1 or bimatch(selected[num]):         
            selected[num] = x                                
            return True                                   
                                                          
    return False  
#변수받기
N=int(input())
inp=list(map(int,input().split()))
first_num=int(inp[0])

same_first_num=[]
diff_first_num=[]
answer=[]
NN = 2000
 
primes = [True] * (NN)
primes[1] = False
for i in range(2, NN):
  if primes[i]:
    for j in range(i*2, NN, i):
      primes[j] = False
#홀짝만들기
for i in range(len(inp)):
    im=int(inp[i])
    if im%2==first_num%2:
        same_first_num.append(im)
    else:
        diff_first_num.append(im)
#정답구하기
# 홀짝개수 다른 경우
if len(same_first_num)!=N//2:
    print("-1")
else:
    #추가 수 설정
    # checklist=check(1000,1001)
    # 짝수 기준 홀수 추가(가장 앞에 있는 숫자를 짝수, 그와 반대를 홀수로 한 것임)
    same_first_num.remove(first_num)
    answer=[]
    first_with=[]
    for i in diff_first_num:
        if isPrime(i+first_num):
            first_with.append(i)
    if N==2:
        if first_with!=[]:
            answer.append(first_with[0])
    else:
        for i in first_with:
            graph=[]
            tmp = i
            diff_first_num.remove(tmp)
            # print(same_first_num)
            # print(diff_first_num)
            for i in range(N//2-1):
                relist=[]
                for j in range(N//2-1):
                    checknum=same_first_num[i]+diff_first_num[j]
                    if isPrime(checknum):
                        relist.append(j)
                graph.append(relist)
            # print(graph)
            selected = [-1]*(N//2-1)
            for i in range(N//2-1):            
                visited = [False] * (N//2-1)      
                bimatch(i)
                result = 0             
                # for i in range(1, (N//2)):  
                for i in range((N//2)-1):  
                    if selected[i] >= 0:         
                        result += 1
            # print(selected)
            if result==N//2-1:
                answer.append(tmp)
            diff_first_num.append(tmp)
    if answer==[]:
        print(-1)
    else:
        answer.sort()
        print(" ".join(map(str,answer)))