N = int(input())
ns = input().split()
v = int(input())
a = 0
for i in range(N):
    X = int(ns[i])
    if X == v :
        a = a + 1
print(a)