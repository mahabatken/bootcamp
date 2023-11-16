#zip(iterables)-она соединяет каждый элемент итериуемых обьектов между собой в тип данных   tuple и врзвращает интератор.
# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300]

# res = list(zip(ls1, ls2))
# print(res)
#-------------------
#all(),any()
#all(Iterable)-Возрашает True, если все элементы интеруемого обьекта истина, иначе False
# ls =[[1, 2], 5, "stroka", True, 1]
# print(all(ls))
#--------------------
#ip = "10.255.12.155"
# ip2 = "10.255.1y.155"

# result = all(x.isdigit() for x in ip.split("."))
# print(result)
#-----------------
#any- возврашает  True если хотябы один элемент истина

# ls = [0, 0, 0, 0]
# print(any(ls))

# ignore = ["rm - rf", "sudo", "reset", 'poweroff']
# command = input("Vvedite komandu:")
# if any(x for x in ignore):
#     raise Exception("you do not have permissions!")

# print("Ok!")

#-----------------
#Анонимные функции- lambda(такие же функции только без названия)
#Lambda фуекция могуть принимать сколько угодно аргументов но всегда возврашает одно выражения

# def sum_of_args(a, b):
#     res = a + b
#     return res

# print(sum_of_args(5, 15))

#lambda a, b: a + b
# func = lambda a, b: a + b
# print(func(5,15))
#-----------------
 
# def myFunc(n):
#     return lambda a: a * n
# myDoubler = myFunc(2)
# myTripler = myFunc(3)
# print(myDoubler(50))
# print(myDoubler(123))
# print(myDoubler(7))
# print(myTripler(55))

# dict_={"Jogn": 50_000, "Jame":100_000, "Aibek":1_000_000, "Aigerim":15}

# res = dict(sorted(dict_.items(),key=lambda x: x[1]))
# print(res)
#---------------------
#map(function,iterable)применяет ко свем элементом iterable функцию которую мы передаем 

# ls = ["one", "two", "three", "four", "five"]
# res = list(map(str.upper,ls))
# print(res)



# for i in range(len(ls)):
#     ls[i] = ls[i].upper()
# print(ls)


# names = ["John", "Sultan", "Jamie", "Raychel", "Aibek"]

# res = list(map(
#            lambda name: f"Hello mr/ms {name}!",
#            names))
# print(res)


# dict_ ={1: 2, 3: 4, 5: 6}

# res = list(map(
#     lambda x: (x[0], str(x[1])),
#     dict_.items()))
# print(res)

#--------------------
 #TODO filter, reduce, enumarate,repeat

#----------------------------------------------------------------------------------
#1
# list_ = [1, 2, 3, 4]
# print(sum (list_))

#2 
# list_ = [1, 2, 3, 4]
# for x in list_:
#     if x > 3:
#      print(x)
#3
# list= [-9, -8, 7, 6]
# for x in list :
#     if x < 0:
#         print(x)
#4
# ls = [65, 11, 22, 33]
# print(list(map(lambda x: x**2, ls  )))
#5
# ls3 = [22, 44, 5, 66, 63, 3, 4, 55]
# res = list(filter(lambda x: x % 2 == 0, ls3))
# print(res)
#6
# ls = ['Airepieje', 'Aielina', 'Adelina', 'Hyrel', 'Akil', 'Altynbek']
# res =list(filter(lambda x: len(x) > 7, ls))
# print(res)
#7
# from functools import reduce

# list_ = [5, 6, 7, 8]
# res = reduce(lambda x, y : x * y, list_)
# print(res)
#8
# ls = [-4, 6, -9, 88, -67]
# chetnye = len([x for x in ls if x % 2 == 0])
# nechetnye = len([x for x in ls if x % 2 != 0])

# print("Количество четных чисел:", chetnye)
# print("Количество нечетных чисел:", nechetnye)     

#9
# list_ = [-1, 2, 3, 0, 5, -3, 7,]
# print(list(map(lambda x: x > 0, list_)))

#10
# from functools import reduce

# names = ["Aky", "Mahabat", "Aika", "Caadat", "Altynbek"]

# longest_name = reduce(lambda x, y: x if len(x) > len(y) else y, names)

# print(longest_name)


#1)Дано: переменная digits = '123456789'

#Необходимо вывести сумму цифр, представленных в виде одного строкового значения '123456789'. Сумма этих цифр составляет 45. Напишите код, который выдаст эту её.
#Подсказка: используйте генератор списка, функцию int(), функцию sum() для суммирования списка, состоящего из чисел.

# digits = '123456789'
# numbers = [int(i) for i in digits]
# print(sum(numbers))

# list comprehension

#2) напишите лямбда функцию
#которая принимает одно число, и возводит его в квадрат

# a = lambda qwerty: qwerty ** 2
# print(a(5))

#3) напишите лямбда функцию которая принимает 2 числа, первое число возводите в степень второго числа
# a = lambda a,b: a**b
# print(a(5, 2))
#4) напишите лямбда функцию 
#которая принимает список имён, и функция должна приветствовать все имена (используйте функцию map)
# names = ["Akylai", "Mahabat", "Ramis", "Aziza", "Aibek"]

# res = list(map(
#         lambda name: f"Hello mr/ms {name}!",
#            names))
# print(res)
#5) напишите лямбда функцию 
# которая принимает список чисел, и она будет фильтровать этот список,
#то есть будет принимать только те числа которые делятся на 5, использовать встроенные функции filter, list

# from functools import reduce

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# squared_numbers = list(map(lambda x: x**2, even_numbers))

# result = reduce(lambda x, y: x + y, squared_numbers)

# print(result)

# TODO filter, reduce, enumarate,repeat

#filter(function, iterable)-> применяется ко всем элементам iterable функцию которую мф передали и возврашает интератор 
# с теми элементами для которых фунция венула True

# ls = ["one", "two", "", "list", "100", "1", "john"]
# res = []
# for x in ls:
#  if x.isdigit():
#   res.append(x)

# print(res)  
# res = list(filter(str.isdigit, ls))
# print(res)

# ls = ["John", "codifay", "aibek", "ono", "bootcfmp", "Kyrgysctan", "moutains", "lala", "vcghbjkhjg"]
# res = list(filter(lambda x: len(x)>5, ls))
# print(res)

# ls = [
#     {"name": "Python", "point": 10},
#     {"name": "C++", "point": 6},
#     {"name": "Java", "point": 8},
#     {"name": "C#", "point":0 },
# ]
# res = list(filter(lambda dict_: dict_["point"]> 7, ls))

# user = [
#     {"username": "John", "comments":["I love you","Really good"]},
#     {"username": "Raychel", "coments":[]},
#     {"username": "Steven", "coments":["Bishkek","Python"]}
#     {"username":"Hello", "coments":[]},
#     {"username": "Kira", "coments":["The best post"]}
# ]
# active_users = list(filter(lambda obj:obj ['comments'], users))
# inactive_users = list(filter(lambda obj : not obj['comments', users]))
# print(active_users)
# print()
# print(inactive_users)

# names = ["Raychel", "Syltan", "Aigerim", "John", "kira", "Bob"]
# new_name = list(
#     map(lambda x: f"Hello Mr/Ms {x}", filter(lambda x:len(x)> 5, names))
# )
# print(new_name)

#enumerate - она пронумерует каждый элемент внутри iterable  ее собственным индексам
# ls = ["one", "two", "three", "four", "five"]
# # res = list(enumerate(ls))
# # print(res)

# for i, x in enumerate(ls):
#     print(f"Index: {i}, Element: {x}!")

# Функция Reduce () принимает функцию и последовательность и возвращает одно значение, рассчитанное следующим образом:
# 1. Первоначально функция вызывается с первыми двумя элементами из последовательности, и результат возвращается.
# 2. Затем функция вызывается снова с результатом, полученным на шаге 1, и следующим значением в последовательности. 
# Этот процесс повторяется до тех пор, пока в последовательности не появятся элементы.

# ls = [1, 2, 3, 4, 5]
# sum_ = reduce(lambda a, b: a + b, ls)
# res = reduce(lambda a, b: a * b, ls)
# print(sum_, res)

# from itertoots import repeat

# for x in repeat(lambda x: x * 5, 5):
    # print(x)


# from itertools import repeat
# from random import choices
# from string import ascii_letters, digits
# from statistics import mean

# symbols = "_()$1%+-@#"
# q_pass = int(input("Vvedite kolichestvo paroli: "))

# result = {
#     f(choices(ascii_letters, k = 10),
#       choices(digits, k=5),
#       choices(symbols, k=2))
#     for f in repeat(lambda a,b,s: "". join(set(a+b+s)), q_pass)
#           }
# print(result)
# print(f"Quatity of passwords:{len(result)}")
# dlina = [len(x) for x in result]
# print(f"Average len : {mean(dlina)}")



#1)

# def is_magical_date(day, month, year):
#     last_two_digits_of_year = year % 100
#     if day * month == last_two_digits_of_year:
#         return True
#     else:
#         return False

# def find_magical_dates_20th_century():
#     magical_dates = []
#     for year in range(1900, 2000):
#         for month in range(1, 13):
#             for day in range(1, 32):
#                 if is_magical_date(day, month, year):
#                     magical_dates.append((day, month, year))

#     return magical_dates

# magical_dates_20th_century = find_magical_dates_20th_century()
# for date in magical_dates_20th_century:
#     print(f"{date[0]}-{date[1]}-{date[2]}")

#2)

# def is_leap_year(year):

#     if (year % 4 == 0) or (year % 100 != 0 and year % 400 == 0):
#         return True
#     else:
#         return False

# def days_in_month(month, year):
   
#     month_days = {
#         1: 31,
#         2: 29 if is_leap_year(year) else 28,
#         3: 31,
#         4: 30,
#         5: 31,
#         6: 30,
#         7: 31,
#         8: 31,
#         9: 30,
#         10: 31,
#         11: 30,
#         12: 31
#     }

#     if month in month_days:
#         return month_days[month]
#     else:
#         return "Неправильный номер месяца"

# month = int(input("Введите номер месяца (от 1 до 12): "))
# year = int(input("Введите год (четыре цифры): "))


# result = days_in_month(month, year)

# if type(result) == int:
#     print(f"В {month}-м месяце {year} года {result} дней.")
# else:
#     print(result)
#4) 

# import random
# from random import choices
# from string import ascii_letters, digits

# def generate_license_plate():
  
#     if random.choice([True, False]):
        
#         letters = ''.join(random.choices(ascii_letters, k=3))
#         digitss = ''.join(random.choices(digits , k=3))
#         return f"{letters}{digitss}"
#     else:
     
#         digitss = ''.join(random.choices(digits, k=4))
#         letters = ''.join(random.choices(ascii_letters, k=3))
#         return f"{digitss}{letters}"

# random_license_plate = generate_license_plate()
# print(f"Случайный номерной знак:", random_license_plate)


