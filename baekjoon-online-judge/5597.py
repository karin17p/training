submit = []
for i in range(31) :
    submit.append(False)

for _i in range(28) :
    a = int(input())
    submit[a] = True

for i in range(1, 31) :
    if not submit[i] :
        print(i)