import random


def spisok(n):
    lst = []
    while len(lst) < n:
        a = random.randint(0, 50)
        b = a + random.randint(1, 20)
        lst.append([a, b])
    return lst


def act_sel(sel: list):
    res = []
    sel.sort(key=lambda x: x[1])
    res.append(sel[0])
    for x in sel:
        if x[0] > res[-1][1]:
            res.append(x)
    return res


def main():
    n = int(input())
    spisok = [list(map(int, input().split())) for _ in range(n)]
    number = act_sel(spisok)
    print(f'Үл огтлолцох хэрчмийн тоо: {len(number)}')
    print(*number, sep=", ")


if __name__ == "__main__":
    main()

sel = spisok(10)
print(sel)
print(act_sel(sel))
