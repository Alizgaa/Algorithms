# Өгөгдсөн тоон дарааллын хамгийн бага тэгш тоог дэлгэц дээр хэвлэ. Хэрэв тийм байхгүй бол -1-г хэвлэ.
def findmineven(seq):
    ans = -1
    flag = False
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (not flag or seq[i] < ans):
            ans = seq[i]
            flag = True
    return ans

n = list(map(int, input().split()))
print(findmineven(n))

