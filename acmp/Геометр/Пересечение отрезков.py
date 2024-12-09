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
        return 1
    elif vec_product > 0:
        return -1
    else:
        return 0


def line_segment_intersection(A, B, C, D):
    AB = [B[0] - A[0], B[1] - A[1]]
    CD = [D[0] - C[0], D[1] - C[1]]
    AC = [C[0] - A[0], C[1] - A[1]]
    CB = [B[0] - C[0], B[1] - C[1]]
    AD = [D[0] - A[0], D[1] - A[1]]
    DB = [B[0] - D[0], B[1] - D[1]]
    CA = [A[0] - C[0], A[1] - C[1]]
    BC = [C[0] - B[0], C[1] - B[1]]
    BD = [D[0] - B[0], D[1] - B[1]]
    massiv1 = [A, B]
    massiv2 = [C, D]
    sort_line1 = sorted(massiv1, key=lambda x: x[0])
    sort_line2 = sorted(massiv2, key=lambda x: x[0])
    if A == C or A == D or B == C or B == D:
        return "Yes"
    if line_and_point(sort_line1[0], sort_line2[0], sort_line2[1]) == 0:

        if sort_line1[0][0] > sort_line2[0][0] and sort_line1[0][0] < sort_line2[1][0]:
            

            return "No"
        else:
            return "Yes"

    if line_and_point(C, A, B) * line_and_point(D, A, B) < 0 and line_and_point(A, C, D) * line_and_point(B, C, D) < 0:
        return "Yes"
    else:
        return "No"


def main():
    # n = int(input())
    # for i in range(n):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    A = [x1, y1]
    B = [x2, y2]
    C = [x3, y3]
    D = [x4, y4]
    print(line_segment_intersection(A, B, C, D))


if __name__ == "__main__":
    main()
