# NEEDS REVIEW, as Codeforces was broken at the time of this code writing.
calls_from_ilia_per_minute, visits_from_artists_per_minute, minutes_in_day = map(int, input().split())

x = calls_from_ilia_per_minute
y = visits_from_artists_per_minute

if minutes_in_day % 2 == 0:
    artists_killed = 1
else:
    artists_killed = 0
for _ in range(minutes_in_day):
    if x == 0 and y == 0:
        artists_killed += 1
        x = calls_from_ilia_per_minute
        y = visits_from_artists_per_minute
    elif x == 0:
        x = calls_from_ilia_per_minute
    elif y == 0:
        y = visits_from_artists_per_minute
    x -= 1
    y -= 1

print(artists_killed)






