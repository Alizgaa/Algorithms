# Өгөгдсөн дарааллын хамгийн сүүлчийн эерэг элемент x-г хэвлэ.(баруун талын) Хэрэв тийм элемент байхгүй бол -1-г хэвлээрэй.
def findx(seq, x):
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x:
            ans = i
    return ans


n = list(map(int, input().split()))
print(findx(n, 3))
