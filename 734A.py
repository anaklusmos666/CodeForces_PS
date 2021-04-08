n = int(input())
s = input()
a, d = 0, 0

for i in s:
    if i == 'A':
        a += 1
    elif i == 'D':
        d += 1

if a > d:
    print('Anton')
elif a == d:
    print('Friendship')
else:
    print('Danik')