import sys
n =int(sys.stdin.readline())

def hanoi(n,st,ed):
    if n==1:
        print(st,ed)
        return 0
    hanoi(n-1,st,6-st-ed)
    print(st,ed)
    hanoi(n-1,6-st-ed,ed)
print(2**n-1)
hanoi(n,1,3)