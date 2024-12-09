def line_equation(A, B):
    if A[0] == B[0]:
        return f'x = {A[0]}'
    else:
        m = (B[0] - A[0]) / (B[1] - A[1])
        return f'y={B[0] - A[0]}/{B[1] - A[1]} * x + {(B[0] * A[1] - B[1] * A[0])/ (B[0] - A[0])}'

def main():
    x1, y1, x2, y2 = map(int, input().split())
    A = [x1, y1]
    B = [x2, y2]

    print(line_equation(A, B))

if __name__ == "__main__":
    main()
