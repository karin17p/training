score_list = {"A+" : 45, "A0" : 40,
        "B+" : 35, "B0" : 30,
        "C+" : 25, "C0" : 20,
        "D+" : 15, "D0" : 10,
        "F" : 0}
total_score = 0
total_credit = 0

for i in range(20) :
    a, credit, grade = input().split()
    credit = int(float(credit))
    if grade == "P" :
        continue
    score = score_list[grade]
    total_score += credit * score
    total_credit += credit

print((total_score / total_credit) / 10)