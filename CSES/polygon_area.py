def area_polygon(polygon):
    """
    Өгөгдсөн функц нь олон өнцөгтийн оройн цэгийн координатыг "Шнурования" аргаар олно.
    :param polygon (list): Олон өнцөгтийн оройн цэгийн координат [[x1,y1], [x2, y2],...]
    :return (float): Олон өнцөгтийн талбайн
    """
    # polygon = sorted(polygon, key=lambda x: x[0])
    s = 0
    for i in range(len(polygon)):
        x1, y1 = polygon[i][0], polygon[i][1]
        x2, y2 = polygon[(i + 1) % (len(polygon))][0], polygon[(i + 1) % (len(polygon))][1]
        s += x1 * y2 - y1 * x2
    return int(abs(s))


def main():
    n = int(input())
    polygon = []
    for i in range(n):
        x1, y1 = map(int, input().split())
        polygon.append([x1, y1])
    print(area_polygon(polygon))


if __name__ == "__main__":
    main()
