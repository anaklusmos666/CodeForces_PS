n = int(input())
x = 0
for i in range(n):
    y = input()
    if y[1] == '+':
        x += 1
    elif y[1] == '-':
        x -= 1
print(x)