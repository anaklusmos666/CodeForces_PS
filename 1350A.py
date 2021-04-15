from math import sqrt
for i in range(int(input())):
    n, k = map(int, input().split())

    if n%2==0:
        n += 2*k
    elif n%2!=0:
        q = int(sqrt(n))    #finding the smallest divisor
        for j in range(3, q+1, 2):
            if n%j == 0:
                x = j
                break
        else:
            x = n

        n += x + 2*(k-1)

    print(n)