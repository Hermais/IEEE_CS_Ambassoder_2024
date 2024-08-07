participants_count = int(input())

participants_scores = []
for _ in range(participants_count):
    participants_scores.append(list(map(int, input().split())))

for before, after in participants_scores:
    if before != after:
        print("rated")
        quit(0)

max_before = float('inf')
for before, after in participants_scores:
    if max_before >= before:
        max_before = before
    else:
        print("unrated")
        quit(0)

print("maybe")