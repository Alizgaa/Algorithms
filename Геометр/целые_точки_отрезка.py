import math


def integer_points(A, B):
    return math.gcd(abs(A[0] - B[0]), abs(A[1] - B[1])) + 1


def main():
    x1, y1, x2, y2 = map(int, input().split())
    A = [x1, y1]
    B = [x2, y2]
    print(integer_points(A, B))


if __name__ == "__main__":
    main()
