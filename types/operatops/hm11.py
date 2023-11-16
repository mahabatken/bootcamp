# def summa_n(n):
#     n = sum(range(1, n + 1))
#     return n

# print(summa_n(5))
#2---------------
# def test(a:int): print("Положительное"if a > 0 else "Отрицательное")
# test(3)

# def positive():
#     print('Положительное')
# def negative():
#     print("Отрицательное")
# def test(a: int):
#     return positive() if a > 0 else negative() 
# test(-11)
#3----------------


# from math import sqrt, pi
 
# print("1-прямоугольник, 2-треугольник, 3-круг")
# figure = input("Выберите фигуру: ")
 
# if figure == '1':
#     print("Длины сторон прямоугольника:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     print("Площадь: %.2f" % (a * b))
# elif figure == '2':
#     print("Длины сторон треугольника:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     c = float(input("c = "))
#     p = (a + b + c) / 2
#     s = sqrt(p * (p - a) * (p - b) * (p - c))
#     print("Площадь: %.2f" % s)
# elif figure == '3':
#     r = float(input("Радиус круга R = "))
#     print("Площадь: %.2f" % (pi * r ** 2))
# else:
#     print("Ошибка ввода")

#4--------------------

# def reverse_num(number):
#         reversed_num = int(str(number)[::-1])
#         return reversed_num

# number = int(input("Enter number: "))
# reversed_num = reverse_num(number)
# print(f"Reversed number: {reversed_num}")
#5--------------------
# def count_coins(coins: list) -> str:
#     l = []

#     coin = {
#         1: 0,
#         5: 0,
#         10: 0,
#         50: 0,
#     }

#     for i in coins:
#         if i == 1:
#             coin[1] += 1
#             l.append(i)
#         elif i == 5:
#             coin[5] += 1
#             l.append(i)
#         elif i == 10:
#             coin[10] += 1
#             l.append(i)
#         elif i == 50:
#             coin[50] += 1
#             l.append(i)
#         else:
#             return 'Нет такого номинала!'
    
#     return f'Монет по 1 копейке: {coin[1]}\nМонет по 5 копеек: {coin[5]}\nМонет по 10 копеек: {coin[10]}\nМонет по 50 копеек: {coin[50]}\nОбщая сумма: {sum(l) / 100} рублей'


# print(count_coins([1, 1, 1, 5, 5, 50]))


