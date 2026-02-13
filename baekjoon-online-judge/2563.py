is_paper : list[list[bool]] = []
for i in range(100) :
    new_row = []
    for j in range(100) :
        new_row.append(False)
    is_paper.append(new_row)

n = int(input())
for k in range(n) :
    a, b = map(int, input().split())
    for i in range(b, b + 10) :
        for j in range(a, a + 10) :
            is_paper[i][j] = True

filled = 0
for i in range(100) :
    for j in range(100) :
        filled += int(is_paper[i][j])
print(filled)