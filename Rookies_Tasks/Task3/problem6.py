matrix = []
i = 0
j = 0

for _ in range(5):
    temp = list(map(int, input().split()))
    if 1 in temp:
        i = _
        j = temp.index(1)
    matrix.append(temp)

# position of center is 2, 2
t_i = t_j = 2

print(abs(t_i - i) + abs(t_j - j))

