k = int(input())
a = sorted(list(map(int, input().split())), reverse=True)

if k>0:
    c, s = 0, 0
    for i in a:
        s += i
        c += 1
        if s>=k:
            print(c)
            break

    else:
        print(-1)
else:
    print(0)