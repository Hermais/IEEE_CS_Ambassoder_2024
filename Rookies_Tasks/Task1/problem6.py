import math

def can_form_square(total_squares):
    sqrt_total = int(math.isqrt(total_squares))
    return sqrt_total * sqrt_total == total_squares

def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        squares = list(map(int, input().strip().split()))
        total_squares = sum(squares)
        if can_form_square(total_squares):
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
