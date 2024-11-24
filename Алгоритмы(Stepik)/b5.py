# F_m + F_(m+1) + ... + F_n нийлбэрийн сүүлчийн цифрийг олоорой.
# F_m + F_(m+1) + ... + F_n = F_(n+2) - F_(m+2)
def last_digit_sum(m, n):
    period = [0, 1]
    i = 2
    while True:
        period.append((period[i - 1] + period[i - 2]) % 10)
        if period[i - 1] == 0 and period[i] == 1:
            result_n = period[(n + 2) % (len(period) - 2)] % 10
            result_m = period[(m + 1) % (len(period) - 2)] % 10
            return (result_n - result_m) % 10
        i += 1

def main():
    m, n = map(int, input().split())
    print(last_digit_sum(m, n))

if __name__ == "__main__":
    main()
