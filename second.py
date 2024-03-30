def form(c_x, c_y):
    """Формула для сортировки"""
    return (c_x ** 2 + c_y ** 2) ** 0.5


with open('space.csv', 'r', encoding='UTF-8') as f:
    """тение файла"""
    data = {}
    name_forms = {}
    col = 0
    for elem in f.readlines()[1:]:
        process = elem.split(',')
        col += 1
        numbers = process[-2].split(' ')
        n1 = 0
        n2 = 0
        if '-' in numbers[0]:
            n1 = int(numbers[0]) * -1
        elif '-' in numbers[-1]:
            n2 = int(numbers[-1]) * -1
        else:
            n1 = int(numbers[0])
            n2 = int(numbers[-1])
        data.setdefault(col, [process[0], form(n1, n2)])



maximum = 0
b = []
"""Нахождение мксимума"""
for i in range(1, len(data) - 1):
    n = int(data[i][-1])
    if n > maximum:
        maximum = n
"""Нахождение минимума"""
for g in range(len(data) - 1, 1, -1):
    m = data[g][-1]
    if m < maximum:
        maximum = m
        print(m)
        b.append(data[g][0])

print(b[:3])
