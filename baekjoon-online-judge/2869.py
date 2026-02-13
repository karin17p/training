a, b, v = map(int, input().split())
result = (v - b) / (a - b)
if result - int(result) > 0 :
    result = int(result) + 1
else :
    result = int(result)
print(result)