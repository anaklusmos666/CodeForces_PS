a = int(input())
i = 0
while i < a:
    s = input()
    i = i + 1
    if len(s) < 11:
        print(s)
    else:
        print(s[0] + str(len(s[1:len(s)-1])) + s[len(s) - 1])