days_count = int(input())

list_days = list(map(int, input().split()))



if list_days[days_count-1] == 15:
    print("DOWN")
elif list_days[days_count-1] == 0:
    print("UP")
elif days_count <= 1:
    print(-1)
elif list_days[days_count-1] > list_days[days_count-2]:
    print("UP")
else:
    print("DOWN")
