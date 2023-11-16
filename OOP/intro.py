# OOP-object oriented programming(обьект орентированного програмирования)
# Целью создания было связать данные с фунциями которые управляют этими даннными
# класс- этот описания того как должен выглядти обьект то естьт в классах мы записываем какими данными и фукциями будет обладать обькет  
# обьект - сущность которую мы создаем от класса у каждого оюьекта есть собственные данные 
# атрибуты- обычные переменные внутри класса (отребуты обьекта)
# методы- фунции внутри класса 
#-----------------------------------
# class Human:
#     age = 0

#     def __init__(self, fisrt_name, last_name, job, citizenship):
#         self.name = fisrt_name + " " + last_name
#         self.job = job
#         self.citizen = citizenship

#     def show_info(self):
#         return f"Name:{self.name}, Age:{self.age}, Job;{self.job}:Citizenship: {self.citizen}"
    

# john = Human("John", "Snow", "King og North", "Northener")
# james = Human("James", "Krik", "programmer", "USA")   

# print(john.show_info())
# print(james.show_info())
# john.age = 24
# james.age = 19
# john.job = "King of Westeros"
# print()
# print(john.show_info())
# print(james.show_info())


#---------------------------

# class Dog :
    #аттрибуты класса
#     age = 0
#     ushi = True

#     def __init__(self, name :str, color:str):
#         """Инициализатор, именно здесь создаются аттрибуты объекта"""
#         # self = ccылка на объект который только что создался
#         self.name = name 
#         self.color = color

#     def bark(self):
#         print(f'{self.name} лает!!')


#     def show_info(self):
#         print(f'Name{self.name}, Age:{self.age}, color:{self.color},ushi:{self.ushi}')

# rex = Dog ('Rex', 'Black')
# pluto = Dog (color="brown", name="Pluto")
# aktosh = Dog ('Aktosh', 'gray')

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()

# rex.age = 2
# pluto.age = 7
# aktosh.age = 1
# aktosh.ushi = False


# rex.bark()
# pluto.bark()
# aktosh.bark()

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()
 

# class Human:
#     def __init__(self, name) -> None:
#         self.name = name 
#         self.golod = 100

#     def walk(self):
#         print(f"{self.name}walking around!")
#         self.golod += 30

#     def work(self):
#         print(f"{self.name}raboty pabotaet!")
#         self.golod += 50

#     def eat(self, meat, finish = True):
#         print(f"{self.name}pokyshela{meat}!")
#         self.golod -= 60 if finish else 30


#     def info(self):
#         print(f"{self.name} --> {self.golod}")


# obj = Human("Raychel")
# obj.info()
# obj.eat("Kruasan")
# obj.eat("Sandwitch", finish=False)
# obj.info()
# obj.walk()
# obj.work()
# obj.info()
# obj.eat("Burger!!!")
# obj.eat("Fried Potato", finish=False)
# obj.info()


# class Car:
#     def __init__(self, brand, model, color) -> None:
#         self.brand = brand
#         self.model = model
#         self.color = color

#     def show_info(self):
#         return f"{self.brand} {self.model} --> {self.color}"
    
#     def __str__(self) -> str:
#         return f"{self.brand} {self.model} --> {self.color}"

# obj = Car("Cgevrolet", "Impala", "Black")
# obj2 = Car("Kia", "K8", "White")
# obj3 = Car("Toyota","Avalon", "Gray")
# print(obj.show_info())
# print(obj2.show_info)
# print(obj3.show_info)     
# print(obj)
# print(obj2)
# print(obj3)

# import random

# class Sniper:
#     health = 100

#     def __init__(self, name) -> None:
#         self.name = name

#     def shoot(self, other):
#         other.health -= 20
#         print(f"Атаковал{self},y {other}осталось{other.health}!")

#     def __str__(self) -> str:
#         return f"{self.name}"  

# sniper = Sniper("John Wick")    
# sniper2 = Sniper("James")

# while sniper.health and sniper2.health:
#     choice = random.randint(1, 2)
#     sniper.shoot(sniper2)if choice == 1 else sniper2.shoot(sniper)


# print(f"{sniper if sniper.health else sniper2} won the game)")



        
#nm------------------------------------
#1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14).
#Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. 
# Tакже класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь 
# фигуры.
# class Circle:
    # default_color = 'синий'
#     pi = 3.14

#     def __init__(self, radius):
#         self.radius = radius
#         self.color = Circle.default_color

#     def calculate_area(self):
#         return Circle.pi * (self.radius ** 2)

# my_circle = Circle(5)

# my_circle.color = 'красный'

# area = my_circle.calculate_area()

# print(f"Цвет круга: {my_circle.color}")
# print(f"Радиус круга: {my_circle.radius}")
# print(f"Площадь круга: {area}")


#2) Создайте класс для песен Song. Каждая песня имеет название, автора и год выпуска. 
#Добавьте три метода show_author, show_title, show_year, выводящие утверждения о каждом атрибуте экземпляра класса Song, например: 
# "Эта песня вышла в 2010 году". Создайте экземпляр класса с вашей любимой песней и примените все методы.
# class Song:
#     def __init__(self, name ,author,year) -> None:
#         self.name = name
#         self.author = author
#         self.year = year

#     def show_title(self):
#         return f'{self.name} {self.author} --> {self.year}'
    
#     def show_author(self):
#         return f'{self.author}'
    
#     def show_year(self):
#         return f'{self.year}'
    

# obj = Song ('Poker Face', 'Ladi Gaga', '2000')
# obj2 = Song ('Swalla', 'Jason Derulo', '2019')
# obj3 = Song ('Dark Horse', 'Katy Perry', '2020')
    
# print(obj.show_title())
# print(obj.show_author())
# print(obj.show_year())

# print(obj2.show_title())
# print(obj2.show_author())
# print(obj2.show_year())

# print(obj3.show_title())
# print(obj3.show_author())
# print(obj3.show_year())


#3) Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании, стоимость посадки, стоимость за каждый пройденный к
#илометр. Также добавьте к классу метод расчитывающий стоимость поездки. Создайте три экземпляра класса Taxi для трех разных компаний 
#Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждом из них.
# class Taxi:
#     def __init__(self, name ,praise,kajdaya) -> None:
#         self.name = name
#         self.praise = praise
#         self.kajdaya = kajdaya

#     def get_summu  (self,km):
#         return f'{self.name} --> {self.praise + self.kajdaya * km } som' 


# obj = Taxi("Namba", 70, 8)
# obj2 =Taxi("Yandex", 60, 9)
# obj3 =Taxi("Jorgo",80, 7)

# print(obj.get_summu(2))
# print(obj2.get_summu(2))
# print(obj3.get_summu(2))

#4) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. Также создайте метод get_info,
#который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
#Затем объявите экземляр класса и вызовите метод.
# class Kontakt:
#     def __init__(self, name,nomer ) -> None:
#         self.name = name
#         self.nomer = nomer
        

#     def get_info(self):
#         return f'{self.name} --> {self.nomer}'
    
#     def __str__(self) -> str:
#         return f'{self.name} --> {self.nomer}'
    
    
# obj = Kontakt('Shasha Belyi','+996703177179')
# obj2 = Kontakt('Nyrel Shamirov', '+996707177177')


# print(obj.get_info())
# print(obj2.get_info())



#5) Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога 
#от зарплаты - 8%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.

# class Salary:
#     def __init__(self,summa, staj,):
#         self.summa = summa
#         self.staj = staj
#         self.nalog = 0.08

#     def nalogi(self):
#         self.nalog = self.summa * self.nalog * self.staj
#         return self.nalog
    
# my_self = Salary(5000,5)
# print(my_self.nalogi())