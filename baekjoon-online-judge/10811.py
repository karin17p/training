N, M = input().split()
N = int(N)
M = int(M)
B = []
for i in range(N + 1) :
    B.append(i)

for a in range(M) :
    i, j = input().split()
    i = int(i)
    j = int(j)
    for k in range((j + 1 - i)//2) :
        L = i + k
        R = j - k
        temp = B[L]
        B[L] = B[R]
        B[R] = temp

for i in range(1, N + 1) :
    print(B[i], end=" ")