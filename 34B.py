# he has to earn money. so he have to buy those TV sets which has a negative value
# so sort the array and calculate the sum for 'm' TV sets.
n, m = map(int, input().split())
a = list(map(int, input().split()))

b = sorted([i for i in a if i<0])
print(abs(sum(b[:m])))