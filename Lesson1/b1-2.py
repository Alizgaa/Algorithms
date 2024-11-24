s = input()
ans = ''
anscount = 0
for now in set(s):
    nowcount = 0
    for j in range(len(s)):
        if now == s[j]:
            nowcount += 1
    if nowcount > anscount:
        ans = now
        anscount = nowcount
print(ans)