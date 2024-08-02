def convert_to_12_hour_format(s):
    hh, mm = s.split(":")
    hh = int(hh)
    period = "AM"

    if hh == 0:
        hh = 12
    elif hh == 12:
        period = "PM"
    elif hh > 12:
        hh -= 12
        period = "PM"

    return f"{hh:02}:{mm} {period}"

def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        print(convert_to_12_hour_format(s))

if __name__ == "__main__":
    main()
