def eratosfen(n):
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, n+1):
        if prime[i]:
            for j in range(i * i, n+1, i):
                prime[j] = False
    return prime[n]


def main():
    n = int(input())
    print(eratosfen(n))


if __name__ == "__main__":
    main()
