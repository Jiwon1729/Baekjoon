N = int(input())
M = int(input())
if M!=0:
    removed_number = list(map(str,input().split()))
else:
    removed_number=[]
a=[]
for i in range(0,5000001):
    for j in removed_number:
        if j in str(i):
            break
    else:
        a.append(i)
answer = abs(N-100)
for num in a:
    answer = min(abs(N-num)+len(str(num)),answer)
print(answer)