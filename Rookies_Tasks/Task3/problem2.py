import re

def contains_all_alphabets(s):
    matches = re.findall(r'[a-zA-Z]', s)
    unique_letters = set(letter.lower() for letter in matches)
    return len(unique_letters) == 26

input()
if contains_all_alphabets(input()):
    print("YES")
else: print("NO")