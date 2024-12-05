# Шулуун дээр $n$ цэг тэмдэглэв. Эдгээрийг цэгүүдийг хучиж болох
# хамгийн цөөн нэгж хэрчмийн тоог олох программ бичээрэй.

def pointsCover(s):
    s.sort()
    res = []
    i = 0
    while i <= len(s) - 1:
        lr = [s[i], s[i] + 1]
        res.append(lr)
        while i <= len(s) - 1 and s[i] <= max(lr):
            i += 1
    return res


def main():
    n = int(input())
    s = [float(i) for i in input().split()]

    print(*pointsCover(s))
    print(len(pointsCover(s)))


if __name__ == "__main__":
    main()
