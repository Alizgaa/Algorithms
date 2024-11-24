n = 53 ** 123 + 65 ** 2222 - 172 ** 12

ans = 0
while n:
    ans += 42 < n % 49 < 48
    n = n // 7
print(ans)

