def findx(seq, x):
    ans = 0
    for i in range(len(seq)):
        if seq[i] > seq[ans]:
            ans = i
    return seq[ans]
