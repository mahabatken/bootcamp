# num = int(input("Vvedite chislo"))

# if num % 2 == 0:
#     print("even!")
# else:
#     print("odd!")   

# print "even" if num % 2 == 0 else "odd"
# print(res)
# print("even" if num % 2 == 0 else "odd")



#ternarnyi operatori это конструкция которая по всоему действию анологична конструкции if/else но при этом записывается в одну строчку
#<выражение если  if   <условие> else<    вырвжений если 
#sentence = input('Vvedite predlogenie')

# if sentence [-1]=="?":
#      res = "Voprositel\"noe!"
# else:
#      res = "Normal one!"

# print(res)          

#еще один вариант короткий 

# res = "Voprositel\"noe!" if sentence[-1] =="?" else
# "Normal one!"


# print(res, res1)

#-------------------------------

# ls = [55, 12, 75, 85, 99, 15, 11]
# print(ls)

# choice = input("Vvedite min/max:").lower().strip()
# res = max(ls) if choice == "max" else min(ls)

# print(res)

# print(num1/num2):



#1
# def проверка_возраста(имя, возраст):
#     if возраст >= 17:
#         print(f"{имя} допущен в клуб.")
#     else:
#         print(f"{имя} не может посетить клуб из-за возраста.")

# проверка_возраста("Мурат", 24)
# проверка_возраста("Эржан", 21)
# проверка_возраста("Карина", 24)
# проверка_возраста("Алтынай", 17)
# проверка_возраста("Айбек", 16)
#1/2
# Введите число от 1 до 10
# n = int(input("Введите число от 1 до 10: "))

# dict_ = {}

# for i in range(1, 501):
#     if i % n == 0:
#         dict_[i] = i**2

# print(dict_)

#2
# numbers = list(range(1, 100))
# print(numbers)
#3
# int_list = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# new_list = [num for num in int_list if num > 0 and num % 2 == 0]
# print(new_list)

#4
# ls = [x**2 for x in range(1, 26)]
# print(ls)
#5
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(x) for x in str_list]
# print(int_list)
#6
# result_list = []

# for i in range(1, 11):
#     if i % 2 == 1:
#         result_list.append(i)
#     else:
#         result_list.append(i ** 2)

# print(result_list)
#7
#result_list = [True if x % 2 == 0 else False for x in range(1, 11)]
# print(result_list)
#8

# names = ['johan', 'sansa', 'micheal', 'ken', 'bakdoolot', 'sanzhar', 'wild']

# for i in range(len(names)):
#     if len(names[i]) < 4:
#         names[i] = "shorter"
#     else:
#         names[i] = "longer"

# print(names)

#9
# students = {
#     'John': {'history': 90, 'math': 95, 'literature': 91},
#     'Rose': {'history': 92, 'math': 96, 'literature': 81},
#     'Kelly': {'history': 84, 'math': 85, 'literature': 87}
# }

# result = {}

# for student, scores in students.items():
#     best_subject = max(scores, key=scores.get)
#     result[student] = best_subject

# print(result)

#10
# my_dict = {"first":{"a": 1},"secon": {"b": 2}}
# my = {k: v for k, y in my_dict.items() for c, v in y.items()}
# print(my)
