def euclid(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        x, y, g = euclid(b, a % b)
        return (y, x - (a//b) *y , g)

result = euclid(30, 12)
print(result)