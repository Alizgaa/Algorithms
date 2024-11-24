# Өгөгдсөн n элемент дахь хоёр дахь хамгийн их тоог ол.
# (Хамгийн их элементийг дарахад үлдэх элементүүдийн хамгийн их элемент)
def findmax2(seq):
    mx1 = max(seq[0], seq[1])
    mx2 = min(seq[0], seq[1])
    for i in range(len(seq)):
        if seq[i]>mx1:
            mx2 = mx1
            mx1 = seq[i]
        elif seq[i] > mx2:
            mx2 = seq[i]
    return (mx1, mx2)
n = list(map(int, input().split()))
print(findmax2(n))


