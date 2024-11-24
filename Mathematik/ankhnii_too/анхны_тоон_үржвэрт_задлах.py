def prime_factors(n):
    if n < 2:
        return n
    else:
        i = 2
        a = []
        while i * i <= n:
            while n % i == 0:
                a.append(i)
                n //= i
            i += 1
        if n > 1:
            a.append(n)
        return a


def main():
    n = int(input())
    print(prime_factors(n))


if __name__ == "__main__":
    main()
