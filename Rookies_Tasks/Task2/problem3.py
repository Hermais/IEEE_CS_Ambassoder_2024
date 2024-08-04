from bisect import bisect_right
# my code exceeds time limit on larger inputs, so by sorting and using binary bisection

number_of_shops = int(input())
price_of_drink_per_shop = sorted(list(map(int, input().split())))

number_of_days_to_buy = int(input())
money_per_day = [int(input()) for _ in range(0, number_of_days_to_buy)]



# Old slow code
# available_shops_to_buy_from = []
# for money in money_per_day:
#     temp= 0
#     for price_drink in price_of_drink_per_shop:
#         if money >= price_drink:
#             temp += 1
#     available_shops_to_buy_from.append(temp)

# better code
for money in money_per_day:
    print(bisect_right(price_of_drink_per_shop, money))



# for _ in range(0, len(available_shops_to_buy_from)):
#     print(available_shops_to_buy_from[_])