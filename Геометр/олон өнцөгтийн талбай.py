n = int(input())
x = []
y = []
for i in range(n):
    x1, y1 = map(int, input().split())
    x.append(x1)
    y.append(y1)

s_1 = 0
s_2 = 0
for i in range(1, n):
    k = x[i - 1] * y[i]
    l = y[i - 1] * x[i]
    s_1 += k
    s_2 += l
s_1 = s_1 + x[len(y) - 1] * y[0]
s_2 = s_2 + y[len(x) - 1] * x[0]
print(abs((s_1 - s_2)) / 2)
