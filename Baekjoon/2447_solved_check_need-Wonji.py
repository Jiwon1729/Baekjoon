import sys
n =int(sys.stdin.readline())

answer=[['*' for _ in range(n)] for i in range(n)]
M = n
cnt= 1
while M>=3:
    M=M/3
    cnt+=1
for i in range(n):
    for j in range(n):
        for k in range(cnt):
            if (3**(k-1))<=i%(3**k)<2*(3**(k-1))and (3**(k-1))<=j%(3**k)<2*(3**(k-1)):
                answer[i][j]=' '

for i in range(n):
    print("".join(map(str,answer[i])))


'''
Recursion code
def d(n):
  if n>1:
    l=d(n//3)
    L=[]
    for s in l:
      L.append(s*3)
    for s in l:
      L.append(s+' '*(n//3)+s)
    for s in l:
      L.append(s*3)
    return L
  return ['*']
print(*d(int(input())),sep='\n')
'''