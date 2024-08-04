n = int(input())

asphalted_horizontal = set()
asphalted_vertical = set()

days = []

for day in range(1, n * n + 1):
    h, v = map(int, input().split())

    if h not in asphalted_horizontal and v not in asphalted_vertical:
        asphalted_horizontal.add(h)
        asphalted_vertical.add(v)
        days.append(day)

print(" ".join(map(str, days)))
