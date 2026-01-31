grid : list[list[int]] = []

for i in range(9):
    line : list[int] = input().split()
    for j in range(9):
        line[j] = int(line[j])
    grid.append(line)

M = -1
y, x = -1, -1

for i in range(9):
    for j in range(9):
        if M < grid[i][j]:
            M = grid[i][j]
            y, x = i, j

print(M)
print(y + 1, x + 1)