for i in range(int(input())):
    s = input()

    c0, c1 = s.count('0'), s.count('1')
    if min(c0, c1)%2 == 0:
        print('NET')
    else:
        print('DA')