n = int(input())
x = list(map(int, input().split()))[1:]
y = list(map(int, input().split()))[1:]

z = set(x).union(set(y))
all_levels = set(range(1, n+1))

if z == all_levels:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')