#2 
# def shorter(phrase):
#     phrase_dict = phrase.split()
#     for i in range(len(phrase_dict)):
#         print(phrase_dict[i][0].upper(), end= "")

# shorter("Кыргызская Республика") 
#1--------------
# import random

# def log_function_call(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         unique_id = id(result)
#         log_entry = f"Функция {func.__name__} была запущена успешно"
#         log_dict[unique_id] = log_entry
#         return result
#     return wrapper

# @log_function_call
# def generate_random_number():
#     random_number = random.randint(1, 100)
#     print(f"Сгенерированное случайное число: {random_number}")
#     return random_number

# log_dict = {}
# generate_random_number()
# print(log_dict)
#3--------------

# def количество_долин(последовательность):
#     уровень_моря = 0
#     количество_долин = 0
#     в_долине = False

#     for шаг in последовательность:
#         if шаг == 'U':
#             уровень_моря += 1
#         else:
#             уровень_моря -= 1

#         if шаг == 'U' and not в_долине and уровень_моря == 0:
#             в_долине = True
#             количество_долин += 1
#         elif шаг == 'D':
#             в_долине = False

#     return количество_долин

# последовательность = "DUDDDUUDUU"
# print(количество_долин(последовательность))




#класс раb
#1
# import math
# def pifagor():
#     a = int(input("Введите 1 катет: "))
#     b = int(input("Введите 2 катет: "))
#     c = a**2 + b**2
#     c1 = f"гипотенуза равна {math.sqrt(c)}"
#     return c1
# print(pifagor())
#2
