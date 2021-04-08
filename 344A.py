n = int(input())
x = []

for i in range(n):
    y = input()
    x.append(y)

count = 1

for i in range(len(x)-1):
    if x[i] != x[i+1]:
        count += 1

print(count)