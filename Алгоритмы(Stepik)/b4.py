    # F_0 + F_1 + ... + F_n нийлбэрийн сүүлчийн цифрийг олоорой.
    # F_0 + F_1 + ... + F_n = F_(n+2) - 1

def last_digit_sum(n):
    period = [0, 1]
    i = 2
    while True:
        period.append((period[i - 1] + period[i - 2]) % 10)
        if period[i - 1] == 0 and period[i] == 1:
            return (period[(n + 2) % (len(period) - 2)] - 1) % 10
        i += 1


def main():
    n = int(input())
    print(last_digit_sum(n))


if __name__ == "__main__":
    main()
