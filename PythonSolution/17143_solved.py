import sys

R, C, M =map(int,sys.stdin.readline().split())
sharks = []
for _ in range(M):
    r, c, s, d, z = map(int,sys.stdin.readline().split())
    r -= 1
    c -= 1
    # print(d)
    if s>0:
        if d<3:
            # print(r,c,s,d,z)
            s = s % (2*(R-1))
        else:
            s = s % (2*(C-1))
    shark = [r,c,s,d,z]
    sharks.append(shark)

fishing_man = -1
Rows = [i for i in range(R)]
Rows = Rows + list(reversed(Rows[1:-1]))
Cols = [i for i in range(C)]
Cols = Cols + list(reversed(Cols[1:-1]))
catch = 0
# print(Rows)
# print(Cols)
sharks = sorted(sharks,key = lambda x: (x[1],x[0],-x[4]))
while fishing_man<C-1:
    # fishing man move
    fishing_man+=1
    # print(fishing_man,'------------')
    # print(sharks)
    for i in range(len(sharks)):
        if sharks[i][1] ==fishing_man:
            catch+=sharks[i][4]
            # print(sharks[i])
            sharks.remove(sharks[i])
            # print(catch)
            break
        elif sharks[i][1] > fishing_man:
            break
    # sharks moving
    for i in range(len(sharks)):
        if sharks[i][3] == 1:
            if (sharks[i][0]-sharks[i][2])%(2*(R-1))>R-1:
                sharks[i][3]=2
            sharks[i][0] = Rows[(sharks[i][0]-sharks[i][2])%(2*(R-1))]
        elif sharks[i][3] == 2:
            if (sharks[i][0]+sharks[i][2])%(2*(R-1))>R-1:
                sharks[i][3]=1
            sharks[i][0] = Rows[(sharks[i][0]+sharks[i][2])%(2*(R-1))]
        elif sharks[i][3] == 3:
            if (sharks[i][1]+sharks[i][2])%(2*(C-1))>C-1:
                sharks[i][3]=4
            # print(sharks[i],"asdfadf")
            sharks[i][1] = Cols[(sharks[i][1]+sharks[i][2])%(2*(C-1))]
        elif sharks[i][3] == 4:
            if (sharks[i][1]-sharks[i][2])%(2*(C-1))>C-1:
                sharks[i][3]=3
            # print(sharks[i],"asdfadf")
            sharks[i][1] = Cols[(sharks[i][1]-sharks[i][2])%(2*(C-1))]
    # sharks eating
    sharks = sorted(sharks,key = lambda x: (x[1],x[0],-x[4]))
    i = 0
    # print(sharks,'sharkeating')
    while i<(len(sharks)-1):
        if (sharks[i][0] == sharks[i+1][0]) and (sharks[i][1] == sharks[i+1][1]):
            sharks.remove(sharks[i+1])
        else:
            i+=1
print(catch)
