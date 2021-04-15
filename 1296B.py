for i in range(int(input())):
    s = int(input())

    ans = s
    while s>=10:
        x = s//10   #return
        s -= x*9    #spending this money
        ans += x
    print(ans)