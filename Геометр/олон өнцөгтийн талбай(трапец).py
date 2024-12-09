n = int(input())
x = []
y = []
for i in range(n):
    x1, y1 = map(int, input().split())
    x.append(x1)
    y.append(y1)

s = 0
for i in range(1, n):
    s += 0.5 * (y[i - 1] + y[i]) * (x[i] - x[i - 1])
s = s + 0.5 * (y[len(y) - 1] + y[0]) * (x[0] - x[len(x) - 1])
print(abs(s))
