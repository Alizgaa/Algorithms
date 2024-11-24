# Фибоначчийн дарааллын n-р гишүүний сүүлчийн цифрийг ол.
def fib_digit(n):
    a = [0] * (n + 1)
    for i in range(0, n + 1):
        if i == 0:
            a[i] = 0
        elif i == 1:
            a[i] = 1
        else:
            a[i] = a[i - 1] % 10 + a[i - 2] % 10
    if n == 0:
        return a[0]
    if n == 1:
        return a[1]
    else:
        return (a[n - 1] + a[n - 2]) % 10


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
