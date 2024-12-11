def cross_product(a, b):
    """
    [a x b] = x1  * y2 - x2 * y1 вектор үржвэр нь a векторын хувьд b векторын чиглэлийг тодорхойлно.

    - [a x b] > 0 : b вектор а-ын хувьд баруун гар талд
    - [a x b] < 0 : b вектор а-ын хувьд зүүн гар талд
    - [a x b] = 0 : b вектор а вектортой коллинеар
    """
    cross_product = a[0] * b[1] - a[1] * b[0]
    return cross_product


def line_and_point(M, A, B):
    """
    Өгөгдсөн функц нь М цэг A ба B цэгүүдийг дайрсан шулууны хувьд ямар байршилтай болохыг тодорхойлно.
    """
    AM = [M[0] - A[0], M[1] - A[1]]
    MB = [B[0] - M[0], B[1] - M[1]]

    vec_product = cross_product(AM, MB)
    if vec_product < 0:
        return "LEFT"
    elif vec_product > 0:
        return "RIGHT"
    else:
        return "TOUCH"


def main():
    n = int(input())
    for i in range(n):
        x0, y0, x1, y1, x2, y2 = map(int, input().split())
        M = [x0, y0]
        A = [x1, y1]
        B = [x2, y2]
        ans = line_and_point(M, A, B)
        print(ans)


if __name__ == "__main__":
    main()