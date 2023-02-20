#230220
import sys

N = int(sys.stdin.readline())
house = []
for i in range(N):
    ho= list(map(int, sys.stdin.readline().split()))
    house.append(ho)

red_f = house[0][0]
green_f = house[0][1]
blue_f = house[0][2]
if N>=3:
    green = [blue_f+house[1][1]]
    blue = [green_f+house[1][2]]
    red = [min(blue_f,green_f)+house[1][0]]
    for i in range(2,N):
        red.append(min(green[i-2],blue[i-2])+house[i][0])
        green.append(min(red[i-2],blue[i-2])+house[i][1])
        blue.append(min(green[i-2],red[i-2])+house[i][2])
    # print(red[N-2])
    answer = red[N-2]

    green = [red_f+house[1][1]]
    red = [green_f+house[1][0]]
    blue = [min(red_f,green_f)+house[1][2]]
    # print(red,green,blue)
    for i in range(2,N):
        red.append(min(green[i-2],blue[i-2])+house[i][0])
        green.append(min(red[i-2],blue[i-2])+house[i][1])
        blue.append(min(green[i-2],red[i-2])+house[i][2])
    # print(red,green,blue)
    # print(blue)
    answer = min(blue[N-2],answer)

    red = [blue_f+house[1][0]]
    blue = [red_f+house[1][2]]
    green = [min(red_f,blue_f)+house[1][1]]
    for i in range(2,N):
        red.append(min(green[i-2],blue[i-2])+house[i][0])
        green.append(min(red[i-2],blue[i-2])+house[i][1])
        blue.append(min(green[i-2],red[i-2])+house[i][2])

    # print(green)
    answer = min(green[N-2],answer)
else:
    red = min(blue_f,green_f)+house[1][0]
    green = min(red_f,blue_f)+house[1][1]
    blue = min(green_f,red_f)+house[1][2]   
    answer=min(blue,red,green)
# print(red_f,green_f,blue_f)
print(answer)