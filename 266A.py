n = int(input())
s = input()
i, count = 1, 0
while i < n:
    if s[i] == s[i-1]:
        count += 1
    i += 1
print(count)