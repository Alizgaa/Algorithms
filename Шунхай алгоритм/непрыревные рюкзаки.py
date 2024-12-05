# Оролт: w_1, w_2, ... , w_n жинтэй , харгалзан c_1, c_2, ... , c_n үнэ бүхий үнэт эдлэл өгөгдөв.
# Хулгайч W кг даац бүхий цүнтэй бөгөөд тэрээр хамгийн өндөр үнэ бүхий үнэ бүх үнэт эдлэл хулгайлахыг хүсэж байв.
# Хулгайчид туслах программ бичээрэй.





def knapsack(a, W):
    s = sorted(a, key=lambda x: x[0] / x[1], reverse=True)
    result = []
    for i in s:
        if W > i[1]:
            result.append(i)
            W -= i[1]
        else:
            result.append([W * (i[0] / i[1]), W])
            break

    return f"{sum(x[0] for x in result):.3f}"


k = knapsack(a, W)

def main():
    n = int(input())
    things = [list(map(int, input().split())) for _ in range(n)]
    pr

