# Фибоначчийн дарааллын n-р гишүүн
def fib(n):
    a = [0] * (n + 1)
    for i in range(0, n + 1):
        if i == 0:
            a[i] = 0
        elif i == 1:
            a[i] = 1
        else:
            a[i] = a[i-1] + a[i - 2]
    return a[n]


def main():
    n = int(input())
    print(fib(n))

if __name__ == "__main__":
    main()
