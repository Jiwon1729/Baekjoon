import copy
N=int(input())
hexa = [1]
for n in range(1,707):
    tmp = 1+5*n+2*n*(n-1)
    hexa.append(tmp)
answer_list = copy.deepcopy(hexa)
answer_list = set(hexa)
answer = 1
over_num = [1000000,146858,130,26,26,26]

while True:
    if N in answer_list:
        break
    else:
        if N>over_num[answer-1]:
            answer = answer+1
            break
        tmp = list(answer_list)
        answer_list = set()
        for i in tmp:
            if i>over_num[answer-1]:
                continue
            for j in hexa:
                if i + j <= over_num[answer-1]:
                    answer_list.add(i+j)
        answer+=1
        # answer_list.sort()
print(answer)