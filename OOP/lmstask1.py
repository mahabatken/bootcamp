

#Автомобиль: создайте класс с именем Car. Метод __init__ () класса Car должен содержать три атрибута: brand, year и color. 
#оздайте метод get_auto(), который выводит информацию об автомобиле, и метод get_year, который выводит возраст авто .
# class Car:

#     def __init__(self, brand, year, color) -> None:
#         self.brand = brand
#         self.year = year
#         self.color = color
#         self.horsepower = 85

#     def get_avto(self):
#         return f"{self.brand} {self.year} --> {self.color}"
    
#     def get_year(self, natural=2023) -> str:
#         self.natural = natural
#         return f"{self.natural - int(self.year)}"
    
#     def add_horsepower(self):
#         if self.brand.lower() in ["mersedes", "bmw", "poshe"]:
#             return self.horsepower + 40
#         return self.horsepower + 20

# obj = Car("Poshe", 1999,"Black")     
# bmw = Car("BMw", 1998, "Red")       
# obj3 = Car("Mersedes", 1990, "Black")
# print(bmw.brand)
# print(bmw.year)
# print(bmw.color)
# print(bmw.horsepower)
# print(bmw.get_avto())
# print(bmw.get_year())
# print(bmw.add_horsepower())
# print(obj.get_avto())
# print(obj3.get_avto())

# Добавьте атрибут horsepower, который равен 85.

# Напишите метод add_horsepower, который всем машинам будет добавлять по 20 л/с, а машинам Mers, Bmw, Poshe по 40 л/с

# Создайте на основе своего класса экземпляр с именем bmw . Выведите три атрибута по отдельности, затем вызовите все методы.

# Два авто: начните с класса из вышеописанного упражнения. Создайте 2 разных экземпляра, вызовите для каждого экземпляра метод get_auto

# Студенты: создайте класс с именем Student. Создайте атрибуты name, age, course. Напишите метод get_student(), который выводит сводку 
# с информацией о студенте . Создайте еще один метод get_birth_year() для вывода информации о годе рождения студента.
# class Student:
#     def __init__(self, name, age, course) -> None:
#         self.name = name
#         self.age = age
#         self.course = course
    
#     def get_student(self):
#         return f"Imya :{self.name}Vozrast:{self.age} ychitca v {self.course}" 

#     def get_birth_year(self):
#         return f"God rojdeniy:{2023 - self.age}"
    
# obj = Student("Altai", 21, "menedjment")
# obj2 = Student("Adilit", 17, "psihologiya")
# obj3 = Student("Atai",20, "bootcamp")   
# print(obj.get_student())
# print(obj2.get_student())
# print(obj3.get_student())
# print(obj.get_birth_year())
# print(obj2.get_birth_year())
# print(obj3.get_birth_year())

     


