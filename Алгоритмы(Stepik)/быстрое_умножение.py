def fastExponentiation(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        y = fastExponentiation(x, n // 2)
        return y * y
    else:
        y = fastExponentiation(x, (n - 1) // 2)
        return y * y * x

x, n = map(int, input().split())
print(fastExponentiation(x, n))
