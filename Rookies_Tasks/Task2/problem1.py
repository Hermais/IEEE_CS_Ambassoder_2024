# possible improvements: using map() for input assgining for r and c
# possible improvements: using list comprehensions for cake input
# not using strings at all and instead just use lists in lists for easy access and modifcations.
r, c = input().split()


cake = []

for row in range(0, int(r)):
    cake.append(input())

# . is edible
# * is eaten
# S is inedible

cakes_eaten=0


def eat_rows(cake: list[str]):
    global cakes_eaten
    for row_index in range(0, int(r)):
        if cake[row_index].find('S') == -1:
            cakes_eaten += cake[row_index].count('.')
            cake[row_index] = '*'*int(c)


def eat_columns(cake: list[str]):
    global cakes_eaten
    for char_index in range(0, int(c)):
        col_contains_S = False
        for row_index in range(0, int(r)):
            if cake[row_index][char_index] == 'S':
                col_contains_S = True
                break
        if not col_contains_S:
            for row_index in range(0, int(r)):
                if cake[row_index][char_index] == '.':
                    cakes_eaten += 1
                    cake[row_index] = replace_char_at_index(cake[row_index], char_index, '*')


def replace_char_at_index(s, index, new_char):
    new_string = s[:index] + new_char + s[index + 1:]
    return new_string


eat_rows(cake)
eat_columns(cake)
#print(cake)
print(cakes_eaten)



