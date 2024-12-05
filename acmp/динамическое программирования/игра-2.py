n = int(input())
x = list(map(int, input().split()))

player_1 = 0
player_2 = 0
i = 0
while len(x)>0:
    if i % 2 == 0:
        player_1 += max(x[0], x[-1])
    else:
        player_2 += max(x[i], x[len(x) - 1 - i])
    le(x) -= 1
if player_1 > player_2:
    print(1)
elif player_1 == player_2:
    print(0)
else:
    print(2)