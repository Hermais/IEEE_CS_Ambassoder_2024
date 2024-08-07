def are_int_digits_unique(num: int):
    return len(set(str(num))) == len(str(num))


def next_larger_int_with_unique_digits(num: int):
    if are_int_digits_unique(num):
        return num

    return next_larger_int_with_unique_digits(num+1)


print(next_larger_int_with_unique_digits(int(input()) + 1))

