n, h = map(int, input().split())
x = list(map(int, input().split()))
width = 0

for i in x:
    if i > h:
        width += 2
    else:
        width += 1

print(width)