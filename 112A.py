s1 = input().lower()
s2 = input().lower()
print((s1>s2) - (s1<s2))
#simple comparing. they return boolean expression.
#True is 1 and False is 0
#when s1 > s2, in the print function it performs True - False means 1 - 0. so it prints 1
#when s1 < s2, in the print function it performs False - True means 0 - 1. so it prints -1
#when s1 = s2, in the print function it performs False - False means 0 - 0. so it prints 0