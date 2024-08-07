def my_inefficient_code():
    entries_count = int(input())

    entries = sorted(list(map(int, input().split())))

    even_entries = []
    odd_entries = []
    for entry in entries:
        if entry % 2 == 0:
            even_entries.append(entry)
        else:
            odd_entries.append(entry)

    odd_sum = 0
    if len(odd_entries) % 2 != 0:
        odd_sum = sum(odd_entries[1:])
    else:
        odd_sum = sum(odd_entries)

    print(odd_sum + sum(even_entries))


# This is chatGPT code that he refined for me. My original code is above.
entries_count = int(input())
entries = list(map(int, input().split()))

even_sum = 0
odd_sum = 0
min_odd = float('inf')
has_odd = False

for entry in entries:
    if entry % 2 == 0:
        even_sum += entry
    else:
        has_odd = True
        odd_sum += entry
        if entry < min_odd:
            min_odd = entry

if has_odd and odd_sum % 2 != 0:
    odd_sum -= min_odd

print(even_sum + odd_sum)
