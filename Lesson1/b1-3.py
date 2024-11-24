s = input()
ans = ''
anscount = 0
dct = {}
for now in s:
    if now not in dct:
        dct[now] = 0
    dct[now] += 1
    if dct[now] > anscount:
        ans = now
        anscount = dct[now]
print(ans)
