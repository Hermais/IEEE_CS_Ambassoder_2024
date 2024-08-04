from typing import List


def represent_by_max_count_of_prime(num: int) -> list[int]:
    represention = []
    while num > 0:
        if num == 3:
            represention.append(3)
            break
        represention.append(2)
        num -= 2

    return represention



if __name__ == "__main__":
    num = int(input())
    representation = represent_by_max_count_of_prime(num)
    print(len(representation))
    represention_txt = str(representation).removeprefix('[').removesuffix(']').replace(',', '')
    print(represention_txt)
