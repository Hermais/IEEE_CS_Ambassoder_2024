def generate_checkerboard(n):
    for i in range(2 * n):
        for j in range(2 * n):
            if (i // 2 + j // 2) % 2 == 0:
                print('#', end='')
            else:
                print('.', end='')
        print()

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        generate_checkerboard(n)
