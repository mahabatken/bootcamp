# magic metods(магические методы)
# dunder meto(double underscode)->__init__\
#служебные методы

# mагия фишка заключается в том что эти методы запускаются 
# без прямого обращения к ним определенные методы могут отвечать за опреденные операторы

# class A:
#     pass 

# obj = A()

#dunder metodы сравнения
# __eq__(self, other)-> 5 == 8
                       # 5.__eq__(8)
# __ne__ -> !=
# __lt__ -> <
# __gt__ -> >
# __le__ -> <=
#__ge__-> >=
# __sub(self, other) -> -
# __mul__ -> * __div__ -> /
# __mol__ _>% __floordiv ->/
# __add__ -> + __pow__-> **  
# class MyClass:
#     def __init__(self, string) -> None:
#         self.string = string


#     def __str__(self) -> str:
#         return self.string

#     def __add__(self, other):
#         print("add worked!!")
#         print(self, "***")
#         print(other, "___")
#         res = self.string +" "+ other.string
#         return MyClass


# obj1 = MyClass("john")
# obj2 = MyClass("Jami")
# obj3 = MyClass("aziza")
# res = obj1 + obj2 + obj3
# print(res, res.string)           


# class Word(str):
#     def __init__(self, word) -> None:
#         self.word = word


#     def __gt__(self, __value: str) -> bool:
#         print("gt сработал")
#         print(self, "!!!")
#         print(__value, "***")
#         return len(self) > len(__value)


# obj1 = Word("John")
# obj2 = Word("HEllo world")
# print(obj1 > obj2)       
#------------------
# дандер метод сторокового отображения обьектов
# __str__--> для отображения стороки которю будут видеть пользователи
# __repr__--> строковую информацию о тоь как создать обьект

# print(eval("6 + 6")) #-> 6 + 6 -> 12
# class Base:
#     def __init__(self, string) -> None:
#         self.string = string

#     def __str__(self) -> str:
#         return f"Обьекты: {self.string}"

#     def __repr__(self) -> str:
#         return 'Base("string")'  


# user = Base("Hello John")
# print(user) 
# a = eval(repr(user))
# print(a)         

#--------------

# конструктор -> __new__(cls)
# инициализатор -> __init__(self)
# дестуктор -> __del__(self)
# from typing import Self

# class Cifra:
#     def __new__(cls, *args, **kwargs) -> Self:
#         numer = abs(args[0])
#         instance = super().__new__(cls)
#         instance.numer = numer
#         return  instance
    

#     def __add__(self, other):
#         res = self.numer + other.numer
#         print(f"Result:{self.numer} + {other.numer} = {res}")
#         return Cifra(res)


# value1 = Cifra(-117) 
# value2 = Cifra(54)
# value3 = Cifra(-7778)
# value1 + value2
# a = value1 + value2       
# value3 + a
# from random import choice
# class Dod:
#     def sound(self):
#         print("Bark")

# class Cat:
#     def sound(self):
#         print("MMM")

# class Parrot:
#     def sound(self):
#         print("say")    


# class Pet:
#     def __new__(cls) :
#         other = choice([Dod, Cat, Parrot])
#         instance = super().__new__(other) 
#         print(f"I\m {type(instance)}")
#         return instance

#     def __init__(self) -> None:
#         print("init was never closed") 

# pet = Pet()
# pet.sound()                       

#singleton
# class Singleton:
#     _instance = None


#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance

#     def __str__(self) -> str:
#         return str(id(self))

# a = Singleton()
# b = Singleton()
# c = Singleton()
# print(a) 
# print(b)
# print(c)
# print (a is b)
# print (a is c)       


# class A:
#     def __del__(self) :
#         choice = input("Are tou sure delete(yes/no):")
#         if choice.lower().strip() == "yes":
#             print("Deleted")
#             del self
#         else:
#             print("Operation denied!")   

# obj = A()
# del obj
# print(obj)
#----------------------1
# class Account:
#     def __init__(self, name, balance, city):
#         self.name = name
#         self.balance = balance
#         self.city = city
#         print(f"Счет создан для {self.name}")

#     def __repr__(self):
#         return f"Имя держателя счета: {self.name}, Баланс: {self.balance}"

#     def __str__(self):
#         return f"Добро пожаловать, {self.name}! Ваш баланс: {self.balance}. Регистрация в филиале банка в городе {self.city}."

#     def __del__(self):
#         print(f"Счет для {self.name} удален. Пока!")


# account = Account("Айткулова Махабат", 8000, "ЧолпонАта")
# print(account)
# del account
#2
# class MyNumber(int):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         result = self.value + other
#         return f"Это сложение и Ваш результат равен {result}"

#     def __sub__(self, other):
#         result = self.value - other
#         return f"Это вычитание и Ваш результат равен {result}"

#     def __mul__(self, other):
#         result = self.value * other
#         return f"Это умножение и Ваш результат равен {result}"

#     def __truediv__(self, other):
#         result = self.value / other
#         return f"Это деление и Ваш результат равен {result}"

# num = MyNumber(5)
# print(num + 3)  
# print(num - 2) 
# print(num * 4)  
# print(num / 2)  

# #3
# class MyList(list):
#     def __getitem__(self, index):
#         if isinstance(index, int):
          
#             if index > 0:
#                 return super().__getitem__(index - 1)
#             else:
#                 raise IndexError("Index must be greater than 0")
#         elif isinstance(index, slice):
            
#             start = index.start - 1 if index.start else None
#             stop = index.stop - 1 if index.stop else None
#             return super().__getitem__(slice(start, stop, index.step))
#         else:
#             raise TypeError("Invalid index type")

# x = MyList([1, 2, 3, 4, 5])
# print(x[1])  
#4

# class Student:
#     def __init__(self, first_name, last_name, grade, scores):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.grade = grade
#         self.scores = scores

#     def average_score(self):
#         total = sum(self.scores.values())
#         return total / len(self.scores)

#     def __lt__(self, other):
     
#         return self.average_score() < other.average_score()

#     def __gt__(self, other):
        
#         return self.average_score() > other.average_score()

#     def __eq__(self, other):
     
#         return self.average_score() == other.average_score()

#     def __le__(self, other):
       
#         return self.average_score() <= other.average_score()

#     def __ge__(self, other):
       
#         return self.average_score() >= other.average_score()


# student1 = Student('Alia', 'Doe', 10, {'math': 100, 'history': 89, 'literature': 88})
# student2 = Student('Atai', 'Smith', 10, {'math': 95, 'history': 92, 'literature': 90})

# if student1 > student2:
#     print(f"{student1.first_name} {student1.last_name} has a higher average score.")
# elif student1 < student2:
#     print(f"{student2.first_name} {student2.last_name} has a higher average score.")
# else:
#     print("Both students have the same average score.")
#5

# class MyNumber(int):
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         result = self.value + other
#         return f"Это сложение и Ваш результат равен {result}"

#     def __sub__(self, other):
#         result = self.value - other
#         return f"Это вычитание и Ваш результат равен {result}"

#     def __mul__(self, other):
#         result = self.value * other
#         return f"Это умножение и Ваш результат равен {result}"

#     def __truediv__(self, other):
#         result = self.value / other
#         return f"Это деление и Ваш результат равен {result}"



# num = MyNumber(5)
# print(num + 3)  
# print(num - 2)
# print(num * 4)  
# print(num / 2) 

#6 
# class Person:
#     def __init__(self, name, phone_numer, cart_numer):
#         self.name = name
#         self._phone_numer = phone_numer
#         self.__cart_numer = cart_numer

# john = Person("John", "+996703177179", "123456")
# print("Имя:", john.name)
# print("Номер телефона:", john._phone_numer)
# print("Номер карты:", john._Person__cart_numer)
#7

# class Person:
#     def __init__(self, name, phone_numer, cart_numer):
#         self.name = name
#         self._phone_numer = phone_numer
#         self.__cart_numer = cart_numer

# john = Person("John", "+996703177179", "123456")
# john.name = None
# john._phone_numer = None
# john._Person__cart_numer = None
# print("Имя:", john.name)
# print("Номер телефона:", john._phone_numer)
# print("Номер карты:", john._Person__cart_numer)
#8
# class Person:
#     def __init__(self, name, phone_numer, cart_numer):
#         self.name = name
#         self._phone_numer = phone_numer
#         self.__cart_numer = cart_numer

#     def validate_name(self, name):
#         if len(name) < 2:
#             return"John"
#         else:
#             return name.capitalize()

# asa = Person("ALINA", "+996703177179", "12123456")
# print("Имя:", asa.name)
# print("Номер телефона:", asa._phone_numer)
# print("Номер карты:", asa._Person__cart_numer)
#9
# class Person:
#     def __init__(self, name, phone_number, card_number):
#         self.name = name  
#         self._phone_number = self.validate_phone_number(phone_number) 
#         self.__card_number = self.validate_card_number(card_number)  # Приватный атрибут

#     def validate_phone_number(self, phone_number):
#         if isinstance(phone_number, int) and str(phone_number).startswith("999"):
#             return phone_number
#         else:
#             return None

#     def validate_card_number(self, card_number):
#         if isinstance(card_number, int) and len(str(card_number)) == 16:
#             return card_number
#         else:
#             return None


# tolik = Person("Tolik", 9995555123456789, 9999999999999999)


# print("Имя:", tolik.name)
# print("Номер телефона:", tolik._phone_number)
# print("Номер карты:", tolik._Person__card_number)
