# 230215
import sys
N = str(sys.stdin.readline())
M = str(sys.stdin.readline())
answer = 0
ans_str = ""
for i in range(len(N)):
    k=answer
    for j in range(len(M)):
        while N[i:i+k]==M[j:j+k] and i+k<len(N) and j+k<len(N):
            if k>answer:
                ans_str=N[i:i+k]
                answer = k
            k=k+1

if answer == 0:
    print(0)
else:
    [print(answer)]
    print(ans_str)

