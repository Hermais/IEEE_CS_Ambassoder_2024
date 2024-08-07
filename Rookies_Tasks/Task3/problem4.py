

contestants_count, winning_place = map(int, input().split())

contestants = list(map(int, input().split()))

score_of_winning_place = contestants[winning_place-1]

if score_of_winning_place == 0 and not contestants[0] > 0:
    print(0)
elif score_of_winning_place == 0 and contestants[0] > 0:
    print(contestants.index(score_of_winning_place))
else:
    contestants.reverse()
    print(len(contestants) - contestants.index(score_of_winning_place))
