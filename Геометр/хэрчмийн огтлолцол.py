def kos(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1


def scalyr(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())

if kos(x2 - x1, y2 - y1, x4 - x3, y4 - y3) == 0 and (
        scalyr(x2 - x1, y2 - y1, x2 - x3, y2 - y3) < 0 or scalyr(x2 - x1, y2 - y1, x2 - x4, y2 - y4) < 0)
    print("Yes")
