with open('space.csv', 'r', encoding='UTF-8') as file_input:
    """Чтение файла"""
    data = {}
    for elem in file_input.readlines()[1:]:
        process = elem.split(',')# разбиение стороки на элементы по запятым
        if '0 0' in process[2]:
            koords = process[-1]
            data.setdefault(process[0], [process[1], process[-1].rstrip()])# добавление данных в словарь data

with open('space_new.txt', 'w', encoding='UTF-8') as file_write:
    """Запись данных в файл"""
    for k, v in data.items():
        s_x = 0
        s_y = 0
        """Преобразаония чисел"""
        if '-' == v[-1][0]:
            x = int(v[-1][1]) * -1
            s_x = len(v[0]) - x
        elif '-' == v[-1][-2]:
            y = int(v[-1]) * -1
            s_y = len(v[0]) - y
        else:
            s_x = len(v[0]) - int(v[-1][0])
            s_y = len(v[0]) - int(v[-1][-1])
        file_write.write(
            f"При получении данных о корабле {k} возникли сбои. Предположительные координаты - {s_x},{s_y}" + '\n')
