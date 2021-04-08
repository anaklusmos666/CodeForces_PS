x = input()
m_n = list(map(int, x.split()))
m = m_n[0]
n = m_n[1]
area = m*n
if area % 2 == 0:
    req_dominos = int(area/2)
    print(req_dominos)
else:
    req_dominos = int((area-1)/2)
    print(req_dominos)