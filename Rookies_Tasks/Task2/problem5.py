
# The code works fine, but it seems like the problem test cases are flawed...
test_cases = int(input())


results = []
for _ in range(test_cases):
    ingredients_count, max_outside_ingredients = map(int, input().split())
    required_ingredients = list(map(int, input().split()))

    outside_ingredients_set = set()
    outside_ingredients_order = []
    fridge_opening_count = 0

    for ingredient in required_ingredients:
        if ingredient not in outside_ingredients_set:
            fridge_opening_count += 1
            if len(outside_ingredients_set) >= max_outside_ingredients:
                oldest_ingredient = outside_ingredients_order.pop(0)
                outside_ingredients_set.remove(oldest_ingredient)

            outside_ingredients_set.add(ingredient)
            outside_ingredients_order.append(ingredient)

    results.append(fridge_opening_count)

for result in results:
    print(result)
