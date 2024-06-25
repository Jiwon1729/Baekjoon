import sys
import copy

push_range_x = [0, -1, 0, 1, 0]
push_range_y = [1, 0, 0, 0, -1]


def push(switch, y, x):
    for i in range(5):
        cur_x, cur_y = x + push_range_x[i], y + push_range_y[i]
        if 0 <= cur_x <= 9 and 0 <= cur_y <= 9:
            switch[cur_y][cur_x] = not switch[cur_y][cur_x]


ans = 101
board = [[False for i in range(10)]for _ in range(10)]

for i in range(10):
    temp = sys.stdin.readline().rstrip()
    for j in range(10):
        if temp[j] == "O":
            board[i][j] = True

for i in range(1 << 10):
    temp_board = copy.deepcopy(board)
    cnt = 0
    for j in range(10):
        if i & (1 << j):
            cnt += 1
            push(temp_board, 0, j)

    for j in range(1, 10):
        for k in range(10):
            if temp_board[j - 1][k]:
                push(temp_board, j, k)
                cnt += 1

    if not any(temp_board[9]):
        ans = min(ans, cnt)

print(ans if ans != 101 else -1)