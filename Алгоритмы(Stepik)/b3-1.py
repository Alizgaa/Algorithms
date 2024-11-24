def pisano_period(m):
    per = [0, 1]
    current = per[0]
    next = per[1]
    period = 0
    while True:
        oldNext = next
        next = (next + current) % m
        per.append(next)
        current = oldNext
        period += 1
        if next == 1 and current == 0:
            return period, len(per)-2

print(pisano_period(10))