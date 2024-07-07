N, M = map(int,input().split())
matrix = []
for i in range(N):
    matrix.append(str(input()))
# 행 공차 / 열 공차 / 시작점 / 개수
answer = -1
for r in range(-N+1,N):
    for l in range(-M+1,M):
        for st_r in range(N):
            for st_l in range(M):
                n = 1
                num = matrix[st_r][st_l]
                ch = int(num)
                if ch == int(ch**(1/2))**2:
                    answer = max(ch,answer)    
                while (st_r+r*n)<N and (st_r+r*n)>=0 and (st_l+l*n)<M and (st_l+l*n)>=0 and (r!= 0 or l!=0):
                    num+=matrix[st_r+r*n][st_l+l*n]
                    n+=1
                    ch = int(num)
                    if ch == int(ch**(1/2))**2:
                        answer = max(ch,answer)
                    ch = int(num[::-1])
                    if ch == int(ch**(1/2))**2:
                        answer = max(ch,answer)
print(answer)
