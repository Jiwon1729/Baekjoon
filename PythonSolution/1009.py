T=int(input())
for i in range(T):
    a,b = map(int,input().split(" "))
    a = a%10
    b = b%4
    if b==0:
        b=4
    answer = (a**b)%10
    if answer == 0:
        answer = 10
    print(answer)
# 2 4 8 6
# 3 9 7 1
# 4 6 4 6
# 5 5 5 5
# 6
# 7 9 3 1
# 8 4 2 6
# 9 1 9 1