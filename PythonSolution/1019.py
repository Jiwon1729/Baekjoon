N = int(input())
answer = [0 for _ in range(10)]
cnt = 0
remained_sum = 0
while True:
    remained = N%10
    N = N//10
    for i in range(10):
        answer[i] = answer[i] + N*(10**cnt)
        if i<remained:
            answer[i] = answer[i] + 10**cnt
        elif i==remained:
            answer[i] = answer[i] + remained_sum+1
    answer[0] = answer[0] - 10**cnt
    if N==0:
        break
    else:
        remained_sum = remained_sum + remained*(10**cnt)
        cnt+=1
    # print(answer)
print((" ").join(map(str,answer)))