def check_columns_for_x(grid, a, b):
    for col in range(b):
        if all(grid[row][col] == 'X' for row in range(a)):
            return True
    return False


def find_winning_combinations(cards):
    possible_dimensions = [(1, 12), (2, 6), (3, 4), (4, 3), (6, 2), (12, 1)]
    results = []

    for a, b in possible_dimensions:
        grid = [cards[i * b:(i + 1) * b] for i in range(a)]
        if check_columns_for_x(grid, a, b):
            results.append(f"{a}x{b}")

    return results


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    t = int(data[0])
    test_cases = data[1:]

    for cards in test_cases:
        results = find_winning_combinations(cards)
        if results:
            print(f"{len(results)} {' '.join(results)}")
        else:
            print("0")


if __name__ == "__main__":
    main()
