import random


def select_answer():
    answer_list = ["A", "B", "C", "D", "E"]
    answer = random.choice(answer_list)
    return answer


n = int(input("Сурагчдын тоо:"))
d = int(input("Туршилтын тоо:"))

answer_key = ["B", "A", "D", 'D', 'B', 'C', "C", 'A', 'A', 'B', 'A', 'E', 'E', 'C', 'D', 'D', 'C', 'B', 'B',
              'D', 'C', 'B', 'E', 'D', 'A', 'C', 'D', "E", "C", "A", 'D', 'A', "E", 'E', 'D', 'B']
total_score = 0
for i in range(d):
    total = 0
    for j in range(n):
        s = 0
        for k in range(0, 36):
            answer = select_answer()
            if answer_key[k] == answer:
                if i <= 7:
                    s += 1
                elif 7 < i <= 27:
                    s += 2
                else:
                    s += 3
            else:
                s -= 0.5
        total += s
    average_total = total / n
    total_score += average_total

print("Average:", total_score / d)
