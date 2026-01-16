a, b, c = input().split()
d = int(input())
a = int(a)
b = int(b)
c = int(c)
X = a * 3600 + b * 60 + c + d
a = X // 3600
p = X % 3600
b = p // 60
c = p % 60
while True :
  if a >= 24 :
    a = a - 24
  else:
    break
print(a, b, c)