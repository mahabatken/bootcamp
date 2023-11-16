# 1 home w
# a = [1, 1, 2.3, 3 -5, 8, -13, -21, 34.5, 55, 89]
# b = [1, 2.3, 3, 4, -5, 6, 7, 8, 9, -10, 11, -12, -13, 34.5]

# c= []

# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#             break
# print(c)
 
# negetive_list = [num for num in common_elements if num < 0]
# print('Список отрицательных чисел:', negetive_list)
# negetive_list_abs = [abs(num) for num in negetive_list]
# print('Список отрицательныз чисел и абсолютными значениями:', negetive_list_abs)

# common_elements[0] = common_elements[0] ** 3
# common_elements[-1] = common_elements[-1] ** 3
# print("Общийсписок после возведение элементовв степень:", common_elements)


#2
# banknotes = ['Абдылас Малдыбаев', 'Бубусара Бейшеналиева', 'Касым Тыныстанов', 'Тоголок Молдо', 'Курманджан Датка', 'Бенджамин Франклин']
# banknotes[5] = 'Токтогул Сатылганов'
# banknotes.extend(['Алыкул Осмонов', 'Саякбай Каралаев', 'Жусуп Баласагын'])
# denomination_to_index = {1: 0, 5: 1, 10: 2, 20: 3, 50: 4, 100: 5, 200: 6, 500: 7, 1000: 8}
# nominal = int(input("Введите номинал банкноты: "))
# if nominal in denomination_to_index:
#     print(banknotes[denomination_to_index[nominal]])
# else:
#     print("Банкноты с введенным номиналом не существует.")


# 3
# вывод дня недели
# print('Сегодня', weekday + '.')
# проверка пятницы и времени
# if day == 5 and hours < 6:
#     remaining_hours = 6 - hours
#     print('Осталось работать', remaining_hours, 'часа')
#     if remaining_hours < 2:
#         print('Можно уйти пораньше!')
# elif hours < 8:
#     remaining_hours = 8 - hours
#     print('Осталось работать', remaining_hours, 'часа')

#4
# number = int(input('Введите число: ')) 
# if number <= 9 and number >= -9: 
#     print('Число однозначное') 
# else: 
#     print('Двухзначное')

#5
# rating = int(input('Что получил по математике? '))
# if rating == 2:
#  print('Плохо. Марш учиться!')
# if rating == 3:
#  print('Плохо. Марш учиться!')
# if rating == 4:
#  print('Молодец! Можешь отдохнуть.')
# if rating == 5:
#  print('Молодец! Можешь отдохнуть.')

#6
# my_list = [1, '2', 3, 4, '5', 'шесть', 'семь']
# converted_list = [int(x) if str(x).isdigit() else len(str(x)) for x in my_list]
# total_sum = sum(converted_list)
# print(f'Сумма всех элементов списка: {total_sum}')
# even_numbers = [x for x in converted_list if x % 2 == 0]
# odd_numbers = [x for x in converted_list if x % 2 != 0]
# print(f'Список четных чисел: {even_numbers}')
# print(f'Список нечетных чисел: {odd_numbers}')


