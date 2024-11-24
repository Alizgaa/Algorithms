def triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        print("YES")
    else:
        print("NO")


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    triangle(a, b, c)
if __name__ == "__main__":
    main()



