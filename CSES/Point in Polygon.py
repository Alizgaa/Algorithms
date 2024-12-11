def point_inside_polygon(point, polygon):
    """
    Өгөгдсөн цэг олон өнцөгтийн дорор орших эсэхийг шалгана.


    Args:
        point (list): Өгөгдсөн цэгийн координат [x,y]
        polygon (list): Олон өнцөгтийн оройн цэгийн координат [(x1, y1),(x2, y2),...]

    returns:
        bool: True or False
    """
    x, y = point[0], point[1]
    n = len(polygon)
    inside = 0

    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        if (x - x1) * (y2 - y1) == (y - y1) * (x2 - x1):
            if (min(x1, x2) <= x and max(x1, x2) >= x) and (min(y1, y2) <= y and max(y1, y2) >= y):
                return "BOUNDARY"
        if (y1 > y) != (y2 > y):
            intersect_x = (y - y1) / (y2 - y1) * (x2 - x1) + x1
            if x < intersect_x:
                inside += 1

    return "INSIDE" if inside % 2 != 0 else "OUTSIDE"


def main():
    n, m = map(int, input().split())
    points = []
    polygon = []
    for i in range(n):
        x, y = map(int, input().split())
        polygon.append((x, y))
    for i in range(m):
        x, y = map(int, input().split())
        points.append([x, y])


    for i in range(m):
        point = [points[i][0], points[i][1]]
        print(point_inside_polygon(point, polygon))


if __name__ == "__main__":
    main()
