#полифморфизм - собственность метода(функция)используется в раззных классов
#широко распространнено определение один интерфейс много реализации

# list.pop
# dict.pop
# set.pop 

# class Cat:
#     def __init__(self) -> None:
#         (self, name, age)
#         self.age = age

# def info(self):
#     print(f"It\"s cat. Cats name is{self.name}), age: {self.age}")

# def make_sound(self):
#     print("мия мия")

# class Dog:
#     def __init__(self) -> None:
#         (self, name, age)
#         self.age = age

# def info(self):
#     print(f"It\"s cat. Dogs name is{self.name}), age: {self.age}")

# def make_sound(self):
#     print("av av")   

# obj1 = Cat("мышык")
# obj1.info()
# obj1.make_sound()

# obj2 = Dog("арстан")
# obj2.meka_sound()
# obj2.info


# class Shepe:
#     def __init__(self) -> None:
#         self.name = name

#     def area(self):
#         pass
#     def info(self):
#         print("Я геометрическая фигура !")


# class Square(Shape):
#     def __init__(self, length)-> None:
#         super().__init__("квадрат")
#         self.len = length 


#     def area(self):
#         return self.len ** 2
    
#     def info(self):
#         super().info()
#         print("все стороны равны и углы все 90 градусов!")

# class Circle(Shepe):
#     def __init__(self, radius) -> None:
#         super().__init__("Окружность" )    
#         self.r = radius


#     def area(self):
#         from math import pi
#         return round(pu * self.r ** 2, 2)

#     def info(self):
#         return super().info()(self):
#         super().info()
#         print("Диаметр равен двум радиусам!")



# a = Square(8)
# b = Circle(4)

# a.info()
# print(a.area())

# b.info()
# print(b.area())
       

# 1) Что такое Полиморфизм в ООП? Привидите
# примеры
# Полиморфизм — очень важная идея в объектно-ориентированном программировании.
# Мы можем использовать идею полиморфизма для методов класса, так как разные классы в
# Python могут иметь методы с одинаковым именем


# 2) Что выполняет следущий код? Какой у него вывод?
# class Mammal:
#     def move(self):
#         print('Двигается')
# class Hare(Mammal):
#     def move(self):
#         print('Прыгает')
# animal = Mammal()
# animal.move()
# hare = Hare()
# hare.move()
# двигается , прыгает




# 3) Чем удобен метод полиморфизм? Где его можно
# применить? 4) Что выводит следующий код?
# class Parent():
#     def __init__(self):
#        print('Parent init')
# def method(self):
#        print('Parent method')
# class Child(Parent): 
#     def __init__(self): 
#       Parent.__init__(self)
#     def method(self):
#       super(Child, self).method()
# child = Child()
# child.method()



# 5) Каким образом можно получить доступ к родительскому методу из дочернего
# класса? 6) Какой вывод у следующего кода?
# class English:
# def greeting(self):
# print ("Hello")
# class French:
# def greeting(self):
# print ("Bonjour")
# def intro(language):
# language.greeting()
# john = English()
# gerard = French()
# intro(john)
# intro(gerard)


# 7) Каким образом реализовать обязательное переопределение родительского метода в
# дочерних классах?


# 8) Каким образом можно намеренно создать ошибку?


# 9) Зависит ли полиморфизм от наследования?
# Как и в других языках программирования, в Python дочерние классы могут наследовать методы и атрибуты
# родительского класса. Мы можем переопределить некоторые методы и атрибуты специально для того, чтобы они соответствовали дочернему классу, и это поведение нам
# известно как переопределение метода(method overriding).
# 10) Является ли переопределение метода __str__(), примером полиморфизма?


#Telega
#1
# my_string = "Пример строки"
# my_list = [1, 2, 3, 4, 5]
# my_dict = {'ключ1': 10, 'ключ2': 20, 'ключ3': 30}


# my_objects = [my_string, my_list, my_dict]


# for obj in my_objects:
#     if isinstance(obj, str):
#         print(f"Длина строки: {len(obj)}")
#     elif isinstance(obj, list):
#         print(f"Длина списка: {len(obj)}")
#     elif isinstance(obj, dict):
#         print(f"Количество элементов в словаре: {len(obj)}")
#2

# class Dog:
#     def voice(self):
#         print("Гав")

# class Cat:
#     def voice(self):
#         print("Мяу")


# dog_instance = Dog()
# cat_instance = Cat()

# def to_pet(pet):
#     pet.voice()

# to_pet(dog_instance)  
# to_pet(cat_instance)  
#3
# class MyInt(int):
#     def __add__(self, other):
#         print("Это сложение")
#         result = super().__add__(other)
#         return result

# class MyString(str):
#     def __add__(self, other):
#         print("Это конкатенация")
#         result = super().__add__(other)
#         return result

# def add_objects(obj1, obj2):
#     return obj1 + obj2


# int_obj1 = MyInt(7)
# int_obj2 = MyInt(10)
# result_int = add_objects(int_obj1, int_obj2)
# print("Результат сложения:", result_int)

# str_obj1 = MyString("Hello, ")
# str_obj2 = MyString("world!")
# result_str = add_objects(str_obj1, str_obj2)
# print("Результат конкатенации:", result_str)
#4
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname

#     def get_info(self):
#         return f"Привет, меня зовут {self.name} {self.surname}"

# class Employee(Person):
#     def __init__(self, name, surname, company, position):
#         super().__init__(name, surname)
#         self.company = company
#         self.position = position

#     def get_info(self):
#         return f"{super().get_info()}, я работаю в компании “{self.company}” на должности “{self.position}”."

# class Student(Person):
#     def __init__(self, name, surname, university, year):
#         super().__init__(name, surname)
#         self.university = university
#         self.year = year

#     def get_info(self):
#         return f"{super().get_info()}, я учусь в {self.university} на {self.year} курсе."

# def get_human_info(person):
#     print(person.get_info())


# person = Person("Иван", "Петров")
# employee = Employee("Иван", "Петров", "Рога и копыта", "директор")
# student = Student("Иван", "Петров", "КГТУ", "3")

# get_human_info(person)
# get_human_info(employee)
# get_human_info(student)
#5
# from abc import ABC, abstractmethod
# import math

# # Создаем абстрактный класс Shape
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass

# # Создаем класс Triangle, наследующийся от Shape
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def get_area(self):
#         return 0.5 * self.base * self.height

# # Создаем класс Square, наследующийся от Shape
# class Square(Shape):
#     def __init__(self, side_length):
#         self.side_length = side_length

#     def get_area(self):
#         return self.side_length ** 2

# # Создаем класс Circle, наследующийся от Shape
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return math.pi * self.radius ** 2

# # Создаем экземпляры каждого класса
# triangle = Triangle(5, 2)
# square = Square(4)
# circle = Circle(5)

# # Вызываем метод get_area() для каждого экземпляра
# print("Площадь треугольника:", triangle.get_area())
# print("Площадь квадрата:", square.get_area())
# print("Площадь круга:", circle.get_area())

