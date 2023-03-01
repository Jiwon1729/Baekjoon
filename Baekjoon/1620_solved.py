import sys
N, M = map(int,sys.stdin.readline().split())
key={}
key2={}
tmp='string'
for i in range(1, N+1):
    tmp2=sys.stdin.readline().strip()
    key[i] = tmp2
    key2[tmp2] = i
for i in range(M):
    s = sys.stdin.readline().strip()
    if 'A'<=s[0]<='z':
        print(key2[s])
    else:
        s=int(s)
        print(key[s])

