#Өгөгдсөн тэмдэгт мөрт хамгийн олон давтагдсан тэмдэгт мөрийг хэвлэ.(Хэрэв хэд хэдэн тэмдэгтхамгийн
#олон удаа давтагдсан бол тэдгээрийн дурын тэмдэгт мөрийг хэвлэ.)
s = input()
ans = ""
anscnt = 0
for i in range(len(s)):
    nowcnt = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            nowcnt += 1
    if nowcnt > anscnt:
        ans = s[i]
        anscnt = nowcnt
print(ans, anscnt)

