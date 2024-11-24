count = 0
for a in range(1, 36):
    for b in range(a, 36):
        for c in range(b, 36):
            if a + b + c == 36:
                if c ** 2 < b ** 2 + a **2:
                    count += 1
                    print(a, b, c)
print(count)