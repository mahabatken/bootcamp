#обработка исключений
#операторы try...except

# Ошибки Errors -> связанные с кодом 
# SyntaxError
# TabError
# IndentationError

# Исключения Exceptions -> связаны с неправельным вводом данных коротые передаются в код
# ValueError
# TypeError
# NameError
# ZeroDivisionError
# IndexError
# KeyError
# ImportError
# BaseException # прородитель всех ошибок
# try:
#     num1 = int(input("Enter the num1: "))
#     num2 =int(input("Enter the num2: "))
#     print(num1 / num2)
# except ValueError:
#     print("Invalid valyse for num!")
# except ZeroDivisionError:
#     print("Cant divide by zero!")    
      

# try
#     <body> # код с вероятным исключением
# except:
#     <body except>сработает е только если ошибка в try
# <else>
#      #<body> срабатывает только если нет ошибок в try
#      <finally>:
# <body>срабвтывае в любои случае 
    


# dict_={1: "one", 2: "two", 3: "theree"}

# try:
#     key = int(input("Vvedite key: "))
#     print(dict_[key])
# except ValueError:
#     print("Invflid value for key!")
# except KeyError:
#     print("Key does not exists!")
# else:
#     print("No errors!")
# finally:
#     print("The end!")      



#-------------------------------------
#отображения ошибки  усли мы не знаем ошибки 
#1. import sys


# ls = [1,2,3,4,5]
# try:
#     index = int(input("Vvedite index: "))
# except:
#     import sys
#     print(f"oops, we catcher{sys.exc_info()[0]}error!")    
#это первый спороп 
#2. Exception as e
# ls = [1,2,3,4,5]
# while True:
#     try:
#         index = int(input("Vvedite index: "))
#         print(ls[index])
#     except Exception as e:
#         print(f"oops we catched{e._class_}error!")
#---------------------------------

# flag = True
# symbol = '0123456789' + '-'  + '.'

# while flag :
#     print()
#     num1 = input('vvedint pervoe  chislo:')
#     num2 = input('vvedint vtoroe  chislo:')
#     try:
#         num1 = float(num1) if '.' in num1 else int(num1)
#         num2 = float(num2) if '.' in num2 else int(num2)
#     except ValueError:
#         print('вы ввели не правильное число!')
#         continue


#     operator = input('Введите операцию(+, -, *, /): ').strip()
#     if operator == '+':
#         print(f'Результат:{num1 + num2}') 
#     elif operator == '-':
#         print(f'Результат:{num1 - num2}') 
#     elif operator == '*':
#         print(f'Результат:{num1 * num2}')
#     elif operator == '/':
#         print(f'Результат:{num1 / num2}' if num2 !=0 else 'На ноль делить нельзя!')
#     else:
#          print('Вы вели не правильный оператор!')

#     choice = input('Хотите продолжить?(yes/no):')
#     if choice.lower().strip() != 'yes':
#         flag = False
#         print("Пока пока!")

#1--------------------------
#try
#     <body> # код с вероятным исключением
# except:
#     <body except>сработает е только если ошибка в try
# <else>
#      #<body> срабатывает только если нет ошибок в try
#      <finally>:
# <body>срабвтывае в любои случае 

       
#2---------------------------

# try:
#     b = 10
#     c = 11
#     print(a)

# except NameError:
#     print("is not defined!")   


#3----------
# try:
#     num1 = int(input("Enter the num1: "))
#     num2 =int(input("Enter the num2: "))
#     print(num1 / num2)
# except ZeroDivisionError:
#     print("Cant divide by zero!")    
      
#4-------------
# try:
#     num1 = int(input("Enter the num1: "))
#     num2 =int(input("Enter the num2: "))
#     print(num1 + num2)
# except ValueError:
#     print("Invflid value for num!")

#5-------------
# dict_={1: "computer", 2: "keyboard", 3: "mouse"}
# try:
#     key = int(input("Vvedite key: "))
#     print(dict_[key])
# except ValueError:
#      print("Invflid value for key!")
# except KeyError:
#     print("Key does not exists!")
# else:
#     print("No errors!")
# finally:
#  print("The end!")         
#6-----------
# ls = [1,2,3,4,5]
# try:
#      index = int(input("Vvedite index: "))
#      print(ls[index])
# except:
#      import sys
#      print(f"oops, we catcher{sys.exc_info()[0]}error!")
#7-------------
# try:
#     num1 = int(input("Enter the num1: "))
#     num2 =int(input("Enter the num2: "))
#     print(num1 / num2)
# except ValueError:
#     print("Invalid valyse for num!")
# except ZeroDivisionError:
#     print("Cant divide by zero!")    
#8-----------
# try:
#     chelovek = int(input("Введите сумму:"))
#     if chelovek < 0:
#         raise ValueError("Сумма не должна быть отрицательным")
#     else:
#         print("Спасибо что ввели.")
# except ValueError as e:
#     print(e)
#9------------
# try:
#     age = int(input("Vvedite cvoi vozrasn;"))
#     if age < 18 :
#         print("dostyp zaprechen")

#     else:
#       print("spacibo!")
# except ValueError:
#     print("Veeden ne korektnyi vozrast")
# finally:
#     print("Do svidanya")
