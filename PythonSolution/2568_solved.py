import sys

N = int(sys.stdin.readline())
lines =[]
for _ in range(N):
    line = list(map(int,sys.stdin.readline().split()))
    lines.append(line)
lines.sort()

def bin_search(num,st,ed):
    while L[st]>num or L[ed]<num or (ed-st)>=2:
        mid=(st+ed)//2
        if L[mid]>num:
            ed=max(st+1,mid-1)
        else:
            st=min(ed-1,mid+1)
    return st+1

def bin_search2(a):
    # print(B)
    start = -1
    end = len(L)
    while start+1<end:
        mid = (start+end)//2
        if L[mid]<a:
            start=mid
        elif L[mid]>a:
            end=mid
        else:
            return mid
    return end

D = [0 for _ in range(N)]
L = [0]
A =[]
answer=[]
cnt = 0

# 점점 증가하는 수열
for  i in range(len(lines)):
    if lines[i][1]>L[-1]:
        cnt+=1
        L.append(lines[i][1])
        D[i] = cnt
    else:
        # tmp = bin_search(lines[i][1],0,len(L)-1)
        tmp = bin_search2(lines[i][1])
        L[tmp] = lines[i][1]
        D[i] = tmp

# 잘라야 하는 전깃줄 갯수
print(len(D)-cnt)

# 잘라야 하는 전깃줄
for i in range(len(D)-1,-1,-1):
    if cnt!=D[i]:
        answer.append(lines[i][0])
    else:
        cnt-=1
answer.sort()

# 잘라야 하는 전깃줄 오름차순 정렬
for i in range(len(answer)):
    print(answer[i])
