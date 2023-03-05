def tsp(n, w):
    memo = [[-1] * (1 << n) for _ in range(n)]
    return solve(0, 1, n, w, memo)

def solve(curr, visited, n, w, memo):
    if visited == (1 << n) - 1:
        return w[curr][0] if w[curr][0] > 0 else float('inf')

    if memo[curr][visited] != -1:
        return memo[curr][visited]

    min_cost = float('inf')

    for next_city in range(n):
        if visited & (1 << next_city) == 0 and w[curr][next_city] > 0:
            cost = w[curr][next_city] + solve(next_city, visited | (1 << next_city), n, w, memo)
            min_cost = min(min_cost, cost)

    memo[curr][visited] = min_cost
    return min_cost

n = int(input())
w = []
for i in range(n):
    w.append(list(map(int, input().split())))

print(tsp(n, w))