N = int(input())
A = list(map(int,input().split(" ")))
B = [ [A[i],[i]] for i in range(len(A))]
B.sort()
C = [ [B[i][1],B[i][0],i] for i in range(len(B))]
C.sort()
answer=[]
for i in C:
    answer.append(i[2])
print((" ").join(map(str,answer)))