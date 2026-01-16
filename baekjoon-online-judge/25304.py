X = int(input())
N = int(input())
z = 0
c = 0
while True :
  if z != N :
    a, b = input().split()
    a = int(a)
    b = int(b)
    c = c + a * b
    z = z + 1
  if z == N :
    break
if c == X :
  print("Yes")
else:
  print("No")