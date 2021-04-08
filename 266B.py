n, tg = map(int, input().split())
s = list(map(lambda i:i, input()))

for t in range(tg):
    i = 0
    while i<n:
        if s[i] == 'B' and i+1 < n and s[i+1] == 'G':
            s[i], s[i+1] = 'G', 'B'
            i += 2
        else:
            i += 1

print(''.join(map(str, s)))