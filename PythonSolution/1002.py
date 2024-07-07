T=int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split(" "))
    if x1==x2 and y1==y2:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        distsquare = (x2-x1)**2+(y2-y1)**2
        if distsquare==(r1-r2)**2 or distsquare==(r1+r2)**2:
            print(1)
        elif distsquare>(r1+r2)**2 or distsquare<(r1-r2)**2:
            print(0)
        else:
            print(2)