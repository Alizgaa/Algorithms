def talbai(x1, y1, x2, y2, x3, y3):
    s = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    return s


def main():
    N = int(input())
    count = 0
    for i in range(N):
        X, Y, X1, Y1, X2, Y2, X3, Y3, X4, Y4 = map(int, input().split())

        s_rectangle = talbai(X1, Y1, X2, Y2, X3, Y3) + talbai(X2, Y2, X3, Y3, X4, Y4)

        s1 = talbai(X, Y, X1, Y1, X2, Y2)
        s2 = talbai(X, Y, X4, Y4, X1, Y1)
        s3 = talbai(X, Y, X2, Y2, X3, Y3)
        s4 = talbai(X, Y, X3, Y3, X4, Y4)
        if s_rectangle == (s1 + s2 + s3 + s4):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
