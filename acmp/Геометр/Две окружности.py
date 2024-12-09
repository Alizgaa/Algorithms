def distance_two_point(A, B):
    return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5


def circle_intersection(O1, r1, O2, r2):
    d = distance_two_point(O1, O2)
    if r1 + r2 >= d and d + r1 >= r2 and d + r2 >= r1:
        return "YES"
    else:
        return "NO"


def main():
    x1, y1, r1 = map(int, input().split())
    x2, y2, r2 = map(int, input().split())
    O1 = [x1, y1]
    O2 = [x2, y2]
    print(circle_intersection(O1, r1, O2, r2))

if __name__ == "__main__":
    main()
