detail = input()
details = list(map(int, detail.split()))
n = details[0]
k = details[1]
mark_input = input()
count = 0
if n >= k:
    marks = list(map(int, mark_input.split()))
    for value in marks:
        if value >= marks[k-1] and value > 0:
            count += 1
    print(count)
else:
    print(count)