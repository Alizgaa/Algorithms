def gcd(a, b, c, d):
    while b > 0:
        if a == c and b == d:
            return b
        if b > a:
            a, b = b, b-a
        if b > 0:
            if b == d and a >= c and c >= a % b and (c - a % b) % b == 0:
                return b
            a %= b

    if b > 0:
        print('YES')
    else:
        print('NO')


def main():
    n = int(input())
    ans = []
    for i in range(n):
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        a = gcd(a, b, c, d)
        ans.append(a)
    for i in range(len(ans)):
        print(ans[i])


if __name__ == "__main__":
    main()
