N, M =map(int,input().split())
cnt = 0
while M!=0:
    if M>=N:
        M=M%N
    else:
        M*=2
        cnt+=M
print(cnt)