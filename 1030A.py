n = int(input())
x = map(int, input().split())

if sum(x) > 0:
    print('HARD')
else:
    print('EASY')