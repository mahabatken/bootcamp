#найти квадпат ,куб, результат деления на 100 любого числа
# num1 = 5
# -> {"num":5, '2':25, "3": 125, "100":0.05}

# num1 = 5
# res = {"num":num1, '2':nym1**2, "3": num2*3, "100":num2 /100}
# print(res)

# num2 = 75
# res = {"num":num3, "2":num3**2, "3": num2*3, "100":num2 /100}
# print(res)

# num3 = 1154
# res = {"num":num3, "2":num3**2, "3": num2*3, "100":num2 /100}
# print(res)

# Dry - Не повторяйся (Don't repeat yourself)

# def  do_operations(num:int):
#     res ={"num":num, '2':num**2, "3": num*3, "100":num /100}
#     print(res)
          
# do_operations(16)
# do_operations(4356)
# do_operations(31)
# do_operations(1298)
# do_operations(567)    
# Функция -это именнованная часть програмы которая содержит в себе определенный блок кода и может вызываться в других частях программы столько раз сколтко угодно


#def name_of_func(<a, b>   #параметры функции)
#   <body>код какая то логика которая будет давать конечный результат 
# <return># оператор который помогает сохранить результат 
# name_of_func (5, 6 # аргументы )

#параметры фунции переменные в которые мы временно сохраняем данные которые передаем при вызове в фунцию доступно только  внутри функции
#аргуменyты функции -это данные которые мы передаем при вызове фунции они попадают в параментры по очередно
  
# print(len("string"))
# def our_len(obj;Iterable)-> int:
#     "возвращаем длинну интерируемого обьекта"
#     print(obj:)
#     i = 0 
#     foritem in obj:
#     i += 1
#     return f"result: {i}"

# ls = [1,2,3,4,5 ]
# str = "Hello world s vami Mahabat Ken"
# print(our_len(ls))
# print(our_len(str1))

# def isEven (num):
#     return True if num % 2 == 0 else False

# result = isEven(15)
# print(result)

# def isEven(num: int)-> bool:
#     "Return True or False while after chikeng number for even!"
#     return True if num % 2 == 0 else False

# result = isEven(456)
# print(result)


#---------------------------------
#default параметры 

# def sum_of_args(a: int, b: int, c: int=0)-> int:
#     """"retyrs sum of divie argyment"""
#     return a + b + c 

# print(sum_of_args(5, 6, 7))
# print(sum_of_args(9, 123, 123))

#----------------------------------
#позиционные и именнованные аргументы 

# def printParams(a, b, c):
#     print(a, "is stored in param a")
#     print(b, "is stored in param a")
#     print(c, "is stored in param a")

# printParams(5, 10, 15)позиционные аргументы(arguments)на анг
# print()
# printParams(b=5, a=10, c=15) именнованные аргументы(keyword )на анг
# print()
# printParams(5, c=10, b=15)
#позиционные должны стоять впеди именновоного  
#---------------
# оператор *
# a = [1,2,3]
# b = [4,5,6]
# c = [*a, *b]
# print(c)
# распаковка все что внутри
# ------------
# def get_some_date(a, b, *args, **kwargs):
#     print("parametry a, b:",a, b)
#     print(f"аргументы:, {args}")
#     print(f"именнованные аргументы: {kwargs}")
# get_some_date(1, 2, 3, 4, c=5)

# def printScores(student : str, *scores):
#     print(F"Name student: {student}!") -> None:
#     """print info about student to terminal"""
#     print(f"Name of student" {student}!) 
#     print(f"AVG:{sum(scores)/ len(scores)}")
#     print(scores, type(scores),"!!!")
#     fox x scores:
#        print("Scores:", x)

# printScores("John Snow"5, 5, 5, 5, 5, 4, 4, 2)  
# 
# 
# 
# def printPetName(owner: str, **pets):
#     print(f"Owner name{owner}!")
#     print(pets, type(pets),"!!!")   
#     for pet in pets:
#         if type(name) ==list:
#             print(f"{pet},*name")
#         else:
#             print(f"{pet}:{name}")  

# printPetName("John Snow", dog="pluto",cat="Garfild",fish=["Nemo","Dori", "Golden"]turle="Leonardo])        

#-----------------------
# from random import  choice, shuffle
# from string import ascii_letters, digits, punctuation

# symbols =  ascii_letters + digits

# def generate_password(len_: int = 8)-> str:
#     """Fuction generates random string for password, parameter len needs to give lenghts of password.if blank len_ = 8"""
#     res =[choice(symbols)for _ in range(len_ -2)]+[choice(punctuation)for _ in range(2)]
#     shuffle(res)
#     return ''.join(res)

# print(generate_password())
# print(generate_password(12))
# print(generate_password(9))    
#-----------------------------------------
# def add_num(a, b):
#     result = a + b
#     return result

# num1 = 5
# num2 = 7
# sum_result = add_num(num1, num2)
# print( sum_result)


#------------------
#1
#def add_num(a, b):
#     result = a + b
#     return result

# num1 = 11
# num2 = 4
# sum_result = add_num(num1, num2)
# print( sum_result)
#2
# def custom_len(input_string):
#     count = 0
#     for _ in input_string:
#         count += 1
#     print(count)

# input_str = "Привет, мир!"
# custom_len(input_str)
#3
# def print_argument_types(arg1, arg2):
#     type_arg1 = type(arg1).__name__
#     type_arg2 = type(arg2).__name__

#     print(f"Тип первого аргумента: {type_arg1}")
#     print(f"Тип второго аргумента: {type_arg2}")

# param1 = 42
# param2 = "Hello"
# print_argument_types(param1, param2)
#4
# def add_num(a, b):
#     result = a / b
#     return result
# num1 = 8
# num2 = 4
# sum_result = add_num(num1, num2)
# print( sum_result)
#5
# def print_dictionary_keys(input_dict):
#     for key in input_dict.keys():
#         print(key)

# my_dict = {'a': 6, 'b': 3, 'c': 9}
# print_dictionary_keys(my_dict)
#6
#def check_number_odd_even(number):
#     if number % 2 != 0:
#         print("It's odd number")
#     else:
#         print("It's even number")

# test_number1 = 8
# test_number2 = 9
# check_number_odd_even(test_number1)
# check_number_odd_even(test_number2)
#7
#def palindrom(str: str) -> str:
#     return 'Palindrom' if str == str[::-1] else 'NE polindrom'


# print(palindrom('komok'))
#8
# print(max(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(min(1, 2, 3, 4, 5, 6, 7, 8, 9)) 


# def maxi(*args):
#     n = 0
#     for i in args:
#         if i > n:
#             n = i
#     return n


# print(maxi(1, 2, 3, 20, 4, 21, 5, 6, 7, 8, 9))
#9
# def product_of_number(*args):
#     n = 1
#     for i in args:
#         n *= i
#     return n

# print(product_of_number([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9)
#10
# def sum_of_number(number):
    
#     sum = 0
    
#     number_str = str(number)
    
#     for number in number_str:
#         sum += int(number)
#     return sum

# number = 1234
# result = sum_of_number(number)
# print('sum of number', number, ':', result)







    


