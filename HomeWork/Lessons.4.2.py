# Список із 3 елементів
import random

numbers = []
new_numbers = []
for i in range(random.randint (3,10)):
    numbers.append(random.randint(1, 10))
new_numbers.append(numbers[0])
new_numbers.append(numbers[2])
new_numbers.append(numbers[-2])

print(new_numbers)
