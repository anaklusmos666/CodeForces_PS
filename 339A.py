s = input()
z = list(map(int, s.split('+')))
z.sort()
print('+'.join(map(str, z)))