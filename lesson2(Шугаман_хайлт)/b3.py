# Өгөгдсөн n элемент бүхий (n>0) дарааллын хамгийн их элементийг ол.

def find_max(seq):
    mx = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > mx:
            mx = seq[i]
    return mx

seq = list(map(int, input().split()))
print(find_max(seq))
