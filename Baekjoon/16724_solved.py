import sys
R, C = map(int, sys.stdin.readline().split())
map_list = []
def find_cycle(i,j,first_value,cnt):
    global answer
    i2=0
    j2=0
    if map_list[i][j]=='R':
        j2+=1
    elif map_list[i][j]=='L':
        j2-=1
    elif map_list[i][j]=='D':
        i2+=1
    elif map_list[i][j]=='U':
        i2-=1

    map_list[i][j]='X'
    check_list[i][j]=cnt
    if check_list[i+i2][j+j2]==cnt:
        answer+=1
    elif map_list[i+i2][j+j2]!='X':
        find_cycle(i+i2,j+j2,first_value,cnt)
        
check_list=[[0 for _ in range(C)] for k in range(R)]
answer = 0
cnt =0
for _ in range(R):
    tmp=list(sys.stdin.readline().strip('\n'))
    map_list.append(tmp)
for i in range(R):
    for j in range(C):
        # print(map_list)
        if map_list[i][j]=='X':
            continue
        else:
            cnt+=1
            tmp = []
            # print(i,j)
            find_cycle(i,j,[i,j],cnt)
print(answer)