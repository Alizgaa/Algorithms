# Фибоначчийн дарааллын n-р гишүүнийг m-д хуваахад гарах үлдэгдэлийг ол.
def pisano(n, m):
    period = [0, 1]
    i = 2
    while True:
        period.append((period[i - 1] + period[i - 2]) % m)
        if period[i - 1] == 0 and period[i] == 1:
            return period[n % (len(period) - 2)]
        i += 1


def main():
    n, m = map(int, input().split())
    print(pisano(n, m))


if __name__ == "__main__":
    main()
