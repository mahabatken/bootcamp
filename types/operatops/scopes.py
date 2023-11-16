#Области видимости  и пространство имен (scopes)
# технология которая опрелеляет контекст имени в рамках которого мы можем его использовать их 4:


# __build_ins (Встроенная область видимости )-> print,len
# global(Глобальная)-Ю область одного файла
# enclosed(не лакальная замкнутая nonlocal)
# locals(локальная)область внутри функции
# x = 200
# def myFunc():
#     print(x)
#     a = 300
#     print(a)
#     return a 
# myFunc()


# a =10 # global
# print # built_in

# def hello():# global
#     a = "Hello"
#     print(a,"Local inside in func")

# hello()
# print(a, "global")

#LEGB - lokal rnclosed global built-in
#-----------------------------------
#enclosed
#замкнутое пространство имен- локальное пространство ,у которого есть внутреее (вложение) локальное пространство 
# x = "global"
# print(x, "1") # global

# def enclosed(): # global
#     x = "enclosed"
#     def lokal():
#         x= "Loral"
#         print(x, "3")

#     print(x, "2")
#     lokal()
#     print(x, "4")

# enclosed()
# print(x, "5")        
# global - позволяет изменять значения глобальной переменной
#nonglobal-> позволяет изменять значения глобальной перем(замкнутой) переменной находясь внутри локальной области 
# var = 0 

# def increment():# LEGB
#     global var
#     var += 1 #var = var +1
#     print(var)

# increment()
# increment()    
# increment()
# increment()
# increment()

# def counter():
#     num = 0
#     def increment():
#         nonlocal num 
#         num += 1
#         return num
#     return increment

# c_steps = counter()
# c_squats = counter()
# print(c_steps()) #1
# print(c_steps()) #2
# print(c_steps()) #3
# print(c_steps()) #4
# print(c_steps()) #4
# print(c_squats())
# print(c_squats())
# print(c_squats())
# print(c_squats())

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# def showStats(heroes, walkers):
#     print()
#     print(f'John Snow ты убил: \n\tгероев: {heroes} \n\tбелых ходоков: {walkers}')
#     print()
    
# counter_heroes = counter()
# counter_walkers = counter()
# heroes = 0
# walkers = 0

# print("Привествую вас, король Севера John Snow, в игре престолов!")
# while True:
#     print('Тебе доступны следующие действия:')
#     print('1-убить героя, 2-убить ходока, 3-статистика, 4-выйти из игры')
#     choice = input('Введите что хотите сделать: ').strip()
#     if choice == '1':
#         heroes = counter_heroes()
#         print('Вы обезглавили Ланистера!')
#     elif choice == '2':
#         walkers = counter_walkers()
#         print('Вы убили белого ходока!')
#     elif choice == '3':
#         showStats(heroes, walkers)
#     elif choice == '4':
#         print('Bye Bye!')
#         break