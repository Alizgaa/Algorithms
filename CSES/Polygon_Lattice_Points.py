import math


def integer_points_in_polygon(polygon):
    """
    Координат нь бүхэл тоо байх олон өнцөгт дотор орших бүхэл тоон
    координат бүхий цэгүүдийн тоог олно.

    :param polygon (list): Олон өнцөгтийн оройн цэгийн координат
    [[x1, y1], [x2, y2],...]
    :return (integer): цэгийн тоо болох бүхэл тоо
    """
    boundary = 0
    n = len(polygon)
    s = 0
    for i in range(n):
        x1, y1 = polygon[i][0], polygon[i][1]
        x2, y2 = polygon[(i + 1) % n][0], polygon[(i + 1) % n][1]
        boundary += math.gcd(abs(x1 - x2), abs(y1 - y2)) - 1
        s += x1 * y2 - x2 * y1
    s = abs(s)
    return int((s - (boundary + n) + 2)/2), boundary + n


def main():
    n = int(input())
    polygon = []
    for i in range(n):
        x, y = map(int, input().split())
        polygon.append([x, y])
    print(integer_points_in_polygon(polygon)[0], integer_points_in_polygon(polygon)[1])


if __name__ == "__main__":
    main()
