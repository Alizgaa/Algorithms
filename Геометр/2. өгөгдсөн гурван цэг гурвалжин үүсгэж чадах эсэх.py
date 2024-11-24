def orientation(x1, y1, x2, y2, x, y):
    return (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)


def is_inside_triangle(x1, y1, x2, y2, x3, y3, x, y):
    d1 = orientation(x1, y1, x2, y2, x, y)
    d2 = orientation(x3, y3, x2, y2, x, y)
    d3 = orientation(x3, y3, x1, y1, x, y)

    if (d1 > 0 and d2 > 0 and d3 > 0) or (d1 < 0 and d2 < 0 and d3 < 0):
        return "Out"
    else:
        return "In"


def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x, y = map(int, input().split())
    answer = is_inside_triangle(x1, y1, x2, y2, x3, y3, x, y)
    print(answer)


if __name__ == "__main__":
    main()
