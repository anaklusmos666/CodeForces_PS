k, n, w = map(int, input().split(' '))
total = 0
i = 0

for i in range(w):
    total = total + ((i+1) * k)

if total > n:
    print(total - n)
else:
    print(0)