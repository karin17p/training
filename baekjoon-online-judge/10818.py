N = int(input())
ns = input().split()
m = 2000000
M = -2000000
for i in range(N):
    X = int(ns[i])
    if m > X :
        m = X
    if M < X :
        M = X
print(str(m), str(M))