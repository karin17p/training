W = input()
L = len(W)
P = True
for i in range(L // 2) :
    if W[i] != W[L - i - 1] :
        P = False
print(int(P))