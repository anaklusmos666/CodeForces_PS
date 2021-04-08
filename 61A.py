x = list(map(lambda i:i, input()))
y = list(map(lambda i:i, input()))
s = ''
for i in range(len(x)):
    if x[i] == y[i]:
        s += '0'
    else:
        s += '1'

print(s)