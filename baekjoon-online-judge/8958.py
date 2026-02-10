n = int(input())
for i in range(n):
    test = input()
    total_score = 0
    plus = 0
    for k in range(len(test)) :
        if test[k] == "O" :
            plus = plus + 1
            total_score = total_score + plus
        else :
            plus = 0
    print(total_score)