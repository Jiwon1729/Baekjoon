# 230214

import sys
N = int(sys.stdin.readline())
def prime(N):
    prime_num= [2,3]
    for i in range(5,N+1):
        for j in prime_num:
            if j>int(i**1/2):
                prime_num.append(i)
                break
            elif i%j == 0:
                break

        else:
            prime_num.append(i)
    return prime_num
def prime_list(n):
    n+=2
    sieve = [True] * (n)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]
prime = prime_list(N)
# print(prime)
answer = 0
for i in range(len(prime)):
    check_num = 0
    for j in range(i,len(prime)):
        # print(check_num)
        check_num+=prime[j]
        if check_num == N:
            answer+=1
            break
        elif check_num>N:
            break

print(answer)