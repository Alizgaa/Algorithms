# Өгөгдсөн дарааллын хамгийн эхний эерэг элемент x-г хэвлэ.(Зүүн талын) Хэрэв тийм элемент байхгүй бол -1-г хэвлээрэй.
def find_x(seq, x):
    ans = -1
    for i in range(len(seq)):
        if ans == -1 and seq[i] == x:
            ans = i
    return ans

print(find_x([-1, -1, -1, -2, 2, 2], -2))

