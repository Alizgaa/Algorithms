def orientation(x1, y1, x2, y2, x3, y3):
    if (x2 - x1) * (y3 - y2) - (x3 - x2) * (y2 - y1) < 0:
        return -1
    else:
        return 1


n = int(input())
x = []
y = []
for i in range(n):
    x1, y1 = map(int, input().split())
    x.append(x1)
    y.append(y1)
s = 0
for i in range(2, n):
    s += orientation(x[i - 2], y[i - 2], x[i - 1], y[i - 1], x[i], y[i])
s = s + orientation(x[len(x) - 2], y[len(y) - 2], x[len(x) - 1], y[len(y) - 1], x[0], y[0])
s = s + orientation(x[len(x) - 1], y[len(y) - 1], x[0], y[0], x[1], y[1])
if s == -n or s == n:
    print("YES")
else:
    print("NO")
