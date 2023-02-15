list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index = 0
max_e = list_numbers[index]
last_index = len(list_numbers) - 1
last = list_numbers[last_index]
# TODO Оформить решение
for i, current in enumerate(list_numbers):
    if current >= max_e:
        index = i
        max_e = current
list_numbers[last_index] = max_e
list_numbers[index] = last
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
