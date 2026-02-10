for a in range(int(input())):
    R, get = input().split()
    R = int(R)

    gen : str = ""
    for each in get:
        for i in range(R) :
            gen += each
    print(gen)