user = input()
c = []
for char in user:
    if char not in c:
        c.append(char)
    else:
        continue
if len(c) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')