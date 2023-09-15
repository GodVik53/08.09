from random import randint
from collections import Counter


N = int(input("Введите количество монет на столе: "))

import random
money = [random.randint(0, 1) for i in range(N)]
print(*money) # выводим рандомно 1 или 0 по колличеству, которое ввели

counted_number = Counter(money)
most_common_number = counted_number.most_common(2)

print(most_common_number[1][0])