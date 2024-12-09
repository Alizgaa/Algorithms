def symmetry(M: list, A: list, B: list):
    if A[0] == B[0]:
        return 2 * (A[0] - M[0]) + M[0], M[1]
    if A[1] == B[1]:
        return M[0], 2 * (B[1] - M[1]) + M[1]


def main():
    x1, y1, x2, y2 = map(int, input().split())
    x0, y0 = map(int, input().split())
    ans = symmetry([x0, y0], [x1, y1], [x2, y2])
    print(ans[0], ans[1])


if __name__ == "__main__":
    main()
