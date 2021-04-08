n = int(input())
passenger, capacity = 0, 0

for i in range(n):
    a, b = map(int, input().split(' '))
    passenger = passenger + (b - a)
    if passenger > capacity:
        capacity = passenger

print(capacity)