n, a, b = map(int, input().split())




def normalize_by(base : int, num : int) -> int:
    if base >= num > 0:
        return num

    if num <= 0:
        num += base
        return normalize_by(base, num)
    else : # num > base
        num -= base
        return normalize_by(base, num)


print(normalize_by(n, a + b))
