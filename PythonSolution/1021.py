N, M =map(int,input().split())
array = []
dq = [i+1 for i in range(N)]
answer = 0
find_num_arr =list(map(int,input().split()))
for find_num in find_num_arr:    
        pop_number = dq[0]
        i = 0
        while pop_number != find_num:
            i = i+1
            pop_number = dq[i]
        if i <= len(dq)//2:
            answer+=i
        else:
            answer+=len(dq)-i
        dq = dq[i+1:]+dq[0:i]
print(answer)