x = int(input())
n = 0
sol = 0
while n < x:
    n += 1
    prob = input().count('1')
    if prob > 1:
        sol += 1
print(sol)