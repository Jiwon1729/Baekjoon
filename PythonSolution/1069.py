X, Y, D, T = map(int,input().split())

distance = (float(X)**2+float(Y)**2)**(1/2)

if D<T:
    answer = distance
else:
    answer = (distance//(D))*(T)
    norm = distance%(D)
    if answer>0:
        answer-=T
        norm+=D
    tmp = min(2*T, T+abs(D-norm),norm)
    answer+=tmp
print("%.20f"%answer)