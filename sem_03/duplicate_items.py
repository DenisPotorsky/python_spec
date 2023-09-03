"""
1. Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
[1, 2, 3, 1, 2, 4, 5] -> [1, 2]
"""

my_lst = [1, 2, 3, 1, 2, 4, 5]
new_lst = []

for element in my_lst:
    if element in new_lst:
        continue
    if my_lst.count(element) > 1:
        new_lst.append(element)

print(new_lst)
