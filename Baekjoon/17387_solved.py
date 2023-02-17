# 230216
import sys

A =list(map(int,sys.stdin.readline().split()))
B =list(map(int,sys.stdin.readline().split()))
v1 = [A[2]-A[0],A[3]-A[1]]
v2 = [B[2]-A[0],B[3]-A[1]]
v3 = [B[0]-A[0],B[1]-A[1]]
v4 = [B[2]-B[0],B[3]-B[1]]
v5 = [A[2]-B[0],A[3]-B[1]]
v6 = [A[0]-B[0],A[1]-B[1]]
minax = min(A[2],A[0])
maxax = max(A[2],A[0])
minbx = min(B[2],B[0])
maxbx = max(B[2],B[0])
minay = min(A[3],A[1])
maxay = max(A[3],A[1])
minby = min(B[3],B[1])
maxby = max(B[3],B[1])
# if v1[1]*v4[0]==v4[1]*v1[0] and v1[1]*v2[0]==v4[1]*v2[0] :
if (v1[0]*v2[1]-v1[1]*v2[0])*(v1[0]*v3[1]-v1[1]*v3[0])==0 and (v4[0]*v5[1]-v4[1]*v5[0])*(v4[0]*v6[1]-v4[1]*v6[0])==0:
    if maxax<minbx or minax>maxbx or maxay<minby or minay>maxby:
        print(0)
    else:
        print(1)
        

elif (v1[0]*v2[1]-v1[1]*v2[0])*(v1[0]*v3[1]-v1[1]*v3[0])<=0 and (v4[0]*v5[1]-v4[1]*v5[0])*(v4[0]*v6[1]-v4[1]*v6[0])<=0 :
    print(1)
# elif (v1[0]*v2[1]-v2[1]*v1[0])*(v1[0]*v3[1]-v3[1]*v1[0])==0 and (v4[0]*v5[1]-v4[1]*v5[0])*(v4[0]*v6[1]-v4[1]*v6[0])==0:
#     print(1)
else:
    print(0)