# Ханануудын хооронд үлдэх усны хэмжээг тооцоолоорой.
n = list(map(int, input().split()))


def isleflood(h):
    maxpos = 0
    for i in range(len(h)):
        if h[i] > h[maxpos]:
            maxpos = i
    ans = 0
    nowm = 0
    for j in range(maxpos):
        if h[j] > nowm:
            nowm = h[j]
        ans += nowm - h[j]

    nowm = 0
    for k in range(len(h) - 1, maxpos, -1):
        if h[k] > nowm:
            nowm = h[k]
        ans += nowm - h[k]

    return ans

print(isleflood(n))
