x, y, w, h = map(int, input().split())

A = w - x
if A > x :
    A = x

B = h - y
if B > y :
    B = y

if A < B :
    print(A)
else :
    print(B)