shovel_price, unique_token_denomination = map(int, input().split())

def calc_min_shovel(count: int):
    if calc_shovel_price_config(count) == 0. or calc_shovel_price_config(count) == 1.:
        return count

    return calc_min_shovel(count+1)


def calc_shovel_price_config(count: int) -> float:

    total_price = shovel_price * count
    covered_price_by_10 = (total_price // 10) * 10
    diff = total_price - covered_price_by_10
    denom_tokens_required = float(diff) / float(unique_token_denomination)

    return  denom_tokens_required

print(calc_min_shovel(1))

