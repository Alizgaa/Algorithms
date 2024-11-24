# Өгөгдсөн өгүүлбэр дэх хамгийн богино үгийг хэвлэ.
def shortwords(words):
    minlen = len(words[0])
    for word in words:
        if len(word) < minlen:
            minlen = len(words)
    ans = []
    for word in words:
        if len(word) == minlen:
            ans.append(word)

    return ' '.join(ans)
