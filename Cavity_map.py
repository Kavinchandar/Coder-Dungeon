n = int(input())
grid = []
for _ in range(n):
    grid.append(input())

for i in range(1, n-1):
    for j in range(1, n-1):
        if grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i][j+1] and grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i+1][j]:
            grid[i] = grid[i][:j] + 'X' + grid[i][j+1:]

for i in grid:
    print(i)
