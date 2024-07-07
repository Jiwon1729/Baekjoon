T = int(input())
era =[True for i in range(10**5+1)]
era[1] = False
for i in range(2,10**5+1):
    tmp = i*2
    if era[i] ==True:
        while tmp<10**5+1:
            era[tmp] = False
            tmp += i
ans=[]
tmp2 = [[1,3,5,7,9],[1,3,7,9],[1,7,9],[3,7,9],[1,3,9],[1,7]]        
num_set =[]
for num in range(101,10**7,2):
    find_num = num
    while True:
        check = 1
        if find_num%2==1 and find_num>9:
            find_num=find_num//10
        else:
            break
        if find_num<=9:
            for j in range(2,int(int(num)**(1/2)+1)):
                if era[j]==True:
                    if int(num)%j==0:
                        check = 0
            for k in range(2,len(str(num))):
                for l in range(len(str(num))-k+1):
                    if era[int(str(num)[l:l+k])] == False:
                        check = 1
                        break
                if check == 1:
                    break
            if check ==0:
                num_set.append(num)
                break
for i in range(T):
    N = str(input())
    if int(N)==10**7:
        N=str(int(N)-1)
    cnt = len(num_set)-1
    while True:
        if num_set[cnt]>int(N):
            cnt-=1
        else:
            answer = num_set[cnt]
            ans.append(answer)
            break
        if cnt==-1:
            answer = -1
            ans.append(answer)
            break
for i in ans:
    print(i)