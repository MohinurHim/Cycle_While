# Нули ничто, отрицание не допустимо!
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Начальное значение
index = 0
# Сравнение текущего индекса и длины списка
while index < len(my_list):
    positive_numbers = my_list[index]
# Увеличиваем индекс на 1, чтобы перейти к следующему элементу
    index = index + 1
    if positive_numbers == 0:
        continue
    elif positive_numbers < 0:
        print('Отрицательное число')
        break
    else:
            print(positive_numbers)

