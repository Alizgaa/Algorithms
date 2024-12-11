def point_inside_polygon(point, polygon):
    """
    Өгөгдсөн цэг олон өнцөгтийн дорор орших эсэхийг шалгана.


    Args:
        point (tuple): Өгөгдсөн цэгийн координат (x,y)
        polygon (list): Олон өнцөгтийн оройн цэгийн координат

    returns:
        bool: True or False
    """
    x, y = point
    n = len(polygon)
    inside = 0

    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        if (x - x1) * (y2 - y1) == (y - y1) * (x2 - x1):
            if (min(x1, x2) <= x and max(x1, x2) >= x) and (min(y1, y2) <= y and max(y1, y2) >= y):
                r

        if (y1 > y) != (y2 > y):
            intersect_x = (y - y1) / (y2 - y1) * (x2 - x1) + x1
            if x < intersect_x:
                inside += 1
    return "YES" if inside % 2 != 0 else "NO"


def main():
    n, x, y = map(int, input().split())
    point = (x, y)
    polygon = []
    for i in range(n):
        x, y = map(int, input().split())
        polygon.append((x, y))
    print(point_inside_polygon(point, polygon))


if __name__ == "__main__":
    main()
