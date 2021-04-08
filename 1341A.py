t = int(input())

for i in range(t):
    n, a, b, c, d = map(int, input().split())

    w1, w2 = n*(a-b), n*(a+b)
    if w2<(c-d) or w1>(c+d):
        print('No')
    else:
        print('Yes')