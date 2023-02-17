matrix = [[1,2],[3,4],[5,6]]
for x in zip(*matrix):
    print(x)

print(*matrix)