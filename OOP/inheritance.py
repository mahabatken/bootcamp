# # Принципы ООП
# 1. Наследование
# 2. Инкапсуляция
# 3. Полиморизм

# 4. Абстракция
# 5. Ассоциация

#---------------------------------------------
# Наследование 
# Позволяет принемать родительское методы и атрибуты 
# дочернему кдассу 

# Родительский класс
# Дочерный клас
#------------------------------------------------------------------

# class Animal:
#     def print_info(self):
#         print("I/ m an Animal!")


# class Lion(Animal):
#     pass

# class Dog(Animal):
#     pass

# simba = Lion()
# simba.print_info()
# print(dir(simba))


# --------------

# class Animal:
#     def say(self):
#         print(f"this Animal name is:{self.name}: {self. golos}")

#         def eat(self):
#             print(f"{self.name} eats:(self.meal)")

# class Lion(Animal):
#     name = "Lion"
#     golos = "roar"
#     meal = "meat"

# class Dod(Animal):
#     name = "dog"
#     golos = "bark"
#     meal = "home meat"

# class Koala(Animal):
#     name = "koala"
#     golos = "roar"
#     meal = "efkalit"

# rex = Dod()
# simba = Lion()
# maris = koala()
# rex.say()
# rex.eat()
# print()
# simba.say()
# simba.eat()
# print()
# maris/set()
# maris.eat()


# class Persen:
#     def info(self):
#         print("I/ m person from Bishkek!")


# class Student(Persen):
#     def info(self):
#         super().info()
#         print("I/m studi in Manas University!")

# class Abult(Persen):
#     def info(self):
#         super().info()
#         print("I/m older than 18 yers! I work 5 days in the week!")


# obj1 = Student()
# obj2 = Abult()

# obj1.info()
# print()
# obj2.info()


# class Laptor:
#     def __init__(self, brand, model, prise) -> None:
#         self.brand = brand
#         self.model = model
#         self.prise = prise 

#     def get_info(self):
#         return{"brand": self.brand, "model":self.model, "prise": self.prise}
# class Aser(Laptor):
#     def __init__(self, model, prise, year, videocart):
#         super().__init__("Aser", model, prise)
#         self.year = year
#         self.video = videocart

#     def get_info(self):
#         repr = super().get_info()
#         repr["year"] = self.year 
#         repr["videocart"] = self.video 
#         return repr 

# class Apple(Laptor):
#     def __init__(self, model, prise, cpu, display):
#         super().__init__("Makbook", model, prise)
#         self.cpu = cpu
#         self.display = display

#     def get_info(self):
#         repr = super().get_info()
#         repr["display"] = self.display 
#         repr["CPU"] = self.cpu
#         return repr   

# acer = Aser("swift", 700, 2022, "nvida")
# print(acer. get_info())


# mac = Apple("Air", 1200, "M2", 13.6)
# print(mac. get_info())
#------------------------------



# """hm 1
# class Class1:
#     def info (self) -> None:
#         print(f"salam aleikym!")
#     def info1(self):
#         print(f"yalekym assalam!")

# class Class2 (Class1):
#     def info(self) -> None:
#         super().info()
#         print(f"kandaiciz")
#     def info1(self):
#         super().info()
#         print(f"jakshi!")

# obj = Class2()
# obj.info()
# obj.info1()
                       
#2
# class A:
#     def info(self)-> None:
#         print(f"Основной функционал")

# class B(A):
#     def info(self)-> None:
#         super().info()
#         print(f"Дополнительные функции") 

# obj = B()
# obj.info()
              
#3
# class MyString(str):
#     def __init__(self, str1):
#         self.str1 = str1

#     def append(self, st):
#         self.str1 = self.str1 + st

#     def __str__(self) -> str:
#         return self.str1
    

# example = MyString('String')
# print(example)
# example.append('hello')
# print(example)

#4
# class MyDict(dict):
#     def get(self, key, default=None):
#         value = super().get(key, default)
#         if value is None:
#             return 'Are you kidding?'
#         return value
# my_dict = MyDict({'key1': 'value1', 'key2': 'value2'})
# result1 = my_dict.get('key1')
# print(result1) 
# result2 = my_dict.get('key3')
# print(result2)

#5
# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def display(self):
#         return f'{self.name} --> {self.age}'
    
# class Student(Person):
#     def __init__(self, name, age, facultet) -> None:
#         super().__init__(name, age)
#         self.facultet = facultet
    
#     def display_student(self):
#         r = super().display()
#         r = f'{r} {self.facultet}'
#         return r

# obj = Student ('Adelina', 18, 'Menedgment')
# obj1 = Student ('Aielina', 17, 'gos upravleniya')
# print(obj.display())
# print(obj.display_student())

# print(obj1.display())
# print(obj1.display_student())  




# 6) Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован 
# метод 
# search_by_name, который должен принимать имя и возвращать список всех совпадений. 
# Создайте экземпляр класса all_contacts и передайте
#  список ваших контактов.
# """ 

# 7. Создайте класс Smartphone, экземпляры класса должны иметь такие свойства - name, color, memory, battery. battery 
# по умолчанию
# должно быть 0. Переопредилите метод str так чтобы при распечатке он выдавал строку с названием и памятью смартфона. 
# У данного класса также должен быть метод charge, который увеличивает значение батареи на указанную величину.
# class Smartphone:
#     def __init__(self, name, color, memory, battery =0) :
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = battery

#     def charge(self, amount):
#         self.battery += amount
#         return self.battery

#     def __str__(self):
#         return f"{self.name} --> Memory: {self.memory}GB"

# my_phone = Smartphone("iPhone 12", "red", 128)
# print(my_phone.charge(50))
# print(my_phone)


# Создайте два дочерних класса от Smartphone - Iphone и Samsung.
# У Iphone должен быть дополнительный аттрибут - ios и метод send_imessage - возвращает строку с сообщением и от 
#какого телефона оно
#  было выслано.
# А у Samsung должен быть дополнительный аттрибут android и метод show_time, который показывает текущее время.
# Создайте объекты от данных классов и примените все методы.
# """

# """
# 8. Создайте класс Spell для магических заклинаний, экземпляры класса имеют два аттрибута - name - название и formula -
#  полное произношение заклинания. 

# У класса есть два метода: get_description() - дает полное описание заклинания и execute() - совершает заклинание.

# Переопределите у класса метод str, чтобы он выдавал вам название, формулу и описание вместе, к примеру:

# Открытие замков: Alohomora
# позволяет магу попасть в любую комнату, 
# способно открыть любую закрытую замочную скважину.

# Наследуя от класса Spell создайте три заклинания,переопределяя в них родительские методы. Создайте объекты этих трех заклинаний. 
# Вызовите все методы
# """

# """
# 9. Напишите класс CustomError который наследуется от встроенного класса исключений Exception. Переопределите init таким образом
# чтобы через экземпляр класса можно было передавать сообщение и создавать новые виды исключений. 
# Создайте исключение от этого класса с сообщением:
# "ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ"

# Напишите функцию проверяющую строки на регистр и если строка не написана в верхнем регистре выбросите исключение созданное классом
#  CustomError:

# Traceback (most recent call last):
#   File "inheritance.py", line 121, in <module>
#     check_letters(a)
#   File "inheritance.py", line 117, in check_letters
#     raise capitals_error
# main.CustomError: ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ

# """

# """
# 10. Создайте класс Character с помощью которого можно создавать героев для игры. Экземпляры класса должны иметь 
# аттрибут name.
#  У класса должна быть переменная power_list, в которой хранится словарь:
# power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }

# Класс должен иметь методы:
# give_weapon - выбирает случайное оружие из списка

# give_role - выбирает случайную роль из списка, к примеру:
# ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]

# give_powers, передавая силу и значение можно менять power_list для определенного героя, к примеру:
# char1.give_powers('ловкость', 5)
# увеличит ловкость вашего героя.

# Создайте три разных дочерьних класса от класса Character - Elf, Orc, DragonBorn, 
# дайте каждому из классов уникальный метод и добавьте уникальные аттрибуты экземпляра класса,наследуя init от Character. 
# Создайте несколько героев от этих классов и вызовите их методы и методы родительского класса Character. 
# import random


# class Character:
#     power_list = {'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0}
#     weapon_list = ['topor', 'balta', 'balka', 'orok', 'airy', 'pila']
#     role_list = ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]

#     def __init__(self, name) -> None:
#         self.name = name

#     def give_weapon(self):
#         return random.choice(self.weapon_list)
    
#     def give_role(self):
#         return random.choice(self.role_list)
    
#     def give_powers(self, type, power):
#         self.power_list[type] += power
#         return self.power_list


# class Elf(Character):
#     def __init__(self, name) -> None:
#         super().__init__(name)
#         self.ushi = 'Ostrye ushi!'
    
#     def strela(self):
#         return 'vistrel'

# class Orc(Character):
#     def __init__(self, name) -> None:
#         super().__init__(name)
#         self.strashnie = "ollo strashnie"

#     def bit(self):
#         return "silno bit"

# class DragonBorn(Character):
#     def __init__(self, name) -> None:
#         super().__init__(name)
#         self.krilya = "bolshie krilya"

#     def letaet(self):
#         return "bistro letaet"
        

# shrek = Elf("Shrek")
# fiona = Orc("fiona")
# osel = DragonBorn("osel")

# print(shrek.give_weapon())
# print(shrek.give_role())
# print(shrek.give_powers('ловкость', random.randint(0, 100)))
# print(shrek.strela())

# print(fiona.give_weapon())
# print(fiona.give_role())
# print(fiona.give_powers('мудрость', random.randint(0, 100)))
# print(fiona.bit())

# print(osel.give_weapon())
# print(osel.give_role())
# print(osel.give_powers('интеллект', random.randint(0, 100)))
# print(osel.letaet())



