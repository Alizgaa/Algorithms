# Өгөгдсөн $[M; N], (2 \le M \le N \le 300 000)$ завсарт харьяалагдах бүх анхны тоог хэвлэх программ бичээрэй.
# Хэрэв уг завсарт анхны тоо байхгүй бол «Absent» үгийг дэлгэц дээр хэвлэ.
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

def main():
    m, n = map(int, input().split())
    is_exist = False
    for i in range(m, n + 1):
        if is_prime(i):
            is_exist = True
            print(i)
    if not is_exist:
        print("Absent")

if __name__ == "__main__":
    main()
