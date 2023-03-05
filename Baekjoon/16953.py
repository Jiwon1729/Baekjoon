import sys
A, B = map(int, sys.stdin.readline().split())
answer = 10**10
def bfs(a,b,k):
    global answer
    queue=[[a,k]]
    while queue:
        tmp2=queue.pop()
        a=tmp2[0]
        k=tmp2[1]
        if k<=answer:
            if a*2== b or a*10+1==b:
                answer=min(k+1,answer)
            else:
                if a*2<b:
                    x = a*2
                    k = k+1
                    tmp=[x,k]
                    # print(tmp)
                    queue.append(tmp)
                if a*10+1<b:
                    x = a*10+1
                    tmp=[x,k]
                    # print(tmp)
                    queue.append(tmp)
    if answer>10**9:
        answer = -2
k = 0
bfs(A,B,k)
print(answer+1)