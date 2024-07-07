import math
N, K = map(int, input().split())
answer = 1
remained_before = N%K
rule = set()
rule.add(remained_before)
if remained_before==0:
    answer = 1
else:
    while True:
        answer+=1
        remained_next = (remained_before*(10**len(str(N))))
        remained_now = (N+remained_next)%K
        if remained_now==0:
            break
        # print(remained_now,remained_next)
        elif remained_now in rule:
            answer=-1
            break
        rule.add(remained_now)
        remained_before = remained_now
print(answer)