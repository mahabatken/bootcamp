# мнжественноне наследования- это когда класс наследуется от двух или болуу классов порядок 
# наследования с  определяется при помощи MPO
# MPO механизм для коректного поиска родитеских методов был созданю.Поиск идеит таким образом что еслти у родитеских
# класов есть общий предок то поиск идет в ширину другими словами сначала у потомков  а потом у ролителя  .

# class Plane:
#     def plany_mysik(self):
#         print("Musik is playing!")


#     def fly(self):
#         print("We\re flying!")


# class Auto:
#     def plany_mysik(self):
#         print("Musik is playing on radio!")


#     def ride(self):
#         print("We\re riding on the ground!")


# class Boat:
#     def play_musik(self):
#         print("Musik is playing on Karaoke!")

#     def swim(self):
#         print('We/re swimming on the sea!')


# class FutureAuto(Auto,Boat, Plane):
#     pass


# obj = FutureAuto()
# obj.fly()
# obj.swim()
# obj.ride()

#---------------------------
# object
# print(object)
# print(dir(object))

# class A:
#     pass

# print(issubclass(A, object))


#-------------------------
#проблема робма - к=огда поиск шел в родительский класс предже чем искать у соседнего потомка, ррешена при помощи MPO
# class Zero:
#     def say(self):
#         print("class Zero")

# class First(Zero):
#     def say(self):
#         print("class First")


# class Sekond(Zero):
#     def say(self):
#         print("class Sekond")


# class Myclass(First, Sekond):
#     pass

# obj = Myclass()
# obj.say()
# print(Myclass.mro())
#------------------------------------------

# проблема перекрестного наследования

# class X:
#     pass

# class Y:
#     pass

# class A(X, Y):
#     pass

# class B(Y, X):
#     pass
# class MyMro(type):
#     def mro(cls):
#         return[cls, A, B, X, Y, object]
       

# class MyClass(A, B):
#     pass

# print(MyClass.mro())

# классная работа

# """Создайте класс Auto в нем реализуйте метод ride который выводит сообщение Riding on a ground, создайте класс 
# Boat реализуйте метод swim, который выводит floating on water.
# Создайте класс Amphibian который наследуется от класса Auto и Boat. Создайте от него объект и вызовите все методы.

# class Auto:
#     def ride(self):
#         print("Riding on a ground")

# class Boat:
#     def swim(self):
#         print("Floating on water")

# class Amphibian(Auto, Boat):
#     pass


# amphibian_vehicle = Amphibian()

# amphibian_vehicle.ride()
# amphibian_vehicle.swim()        




# """Создайте класс RadioMixin в нем реализуйте метод для проигрывания музыки play_music который принимает в 
# себя название песни. Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина"""
 
# class RadioMixing:
#     def play_music(self, name):   
#         return f'{name} Play'


# class Auto(RadioMixing):
#     def play_music(self, name):
#         a = super().play_music(name)
#         a = f'{a} in Auto'
#         return a

# class Boat(RadioMixing):
#     def play_music(self, name):
#         c =  super().play_music(name)
#         c = f'{c} in Boat'
#         return c
    
    
# class Amphibian(RadioMixing):
#     def play_music(self, name):
#         b = super().play_music(name)
#         b = f'{b} in Amphibian'
#         return b



# a = Auto()
# print(a.play_music('Атабеков Мирбек- Сурдотпочу'))
# c = Boat()
# print(c.play_music('Гульнур Сатылганова - Турналар'))
# b = Amphibian()
# print(b.play_music('Омар - Кыргызстаным'))


# """Будильник
# Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения 
# и выключения будильника.
# Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
# нему метод для установки будильника, при вызове которого должен включатся будильник."""

# from datetime import datetime


# class Clock:
#     def datetime(self):
#         return f'{datetime.now().hour}:{datetime.now().minute}'

# class Alarm:
#     def turn_off(self):
#         return 'Выкл'

#     def turn_on(self):
#         return 'Вкл'

# class AlarmClock(Clock, Alarm):
#     def alarm_clock(self, hour, minute):
#         return f'Будильник {self.turn_on()} на {hour}:{minute}'

# p = AlarmClock()
# print(p.alarm_clock(6, 00))


# """Разработчики
# Напишите класс Coder с атрибутами experience, count_code_time = 0 и абстрактными методами
# get_info и coding.
# Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. Класс Backend
#  должен принимать дополнительно параметр languages_backend, а Frontend — languages_frontend соответственно.
# Переопределите в обоих классах методы get_info и coding (так, чтобы он принимал количество часов кодинга и при 
# каждом вызове этого метода добавлял это значение к count_code_time). 
# Так же бывают FullStack разработчики и
# поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов. Создайте несколько
#  экземпляров от классов Backend, Frontend, FullStack и вызовите их методы."""


# from abc import ABC, abstractmethod

# class Coder(ABC):
#     def __init__(self, experience=0):
#         self.experience = experience
#         self.count_code_time = 0

#     @abstractmethod
#     def get_info(self):
#         pass

#     @abstractmethod
#     def coding(self, hours):
#         pass

# class Backend(Coder):
#     def __init__(self, experience=0, languages_backend=[]):
#         super().__init__(experience)
#         self.languages_backend = languages_backend

#     def get_info(self):
#         return f"Backend Developer with {self.experience} years of experience in {', '.join(self.languages_backend)}"

#     def coding(self, hours):
#         self.count_code_time += hours

# class Frontend(Coder):
#     def __init__(self, experience=0, languages_frontend=[]):
#         super().__init__(experience)
#         self.languages_frontend = languages_frontend

#     def get_info(self):
#         return f"Frontend Developer with {self.experience} years of experience in {', '.join(self.languages_frontend)}"

#     def coding(self, hours):
#         self.count_code_time += hours

# class FullStack(Backend, Frontend):
#     def __init__(self, experience=0, languages_backend=[], languages_frontend=[]):
#         Backend.__init__(self, experience, languages_backend)
#         Frontend.__init__(self, experience, languages_frontend)

#     def get_info(self):
#         return f"FullStack Developer with {self.experience} years of experience in Backend: {', '.join(self.languages_backend)}, Frontend: {', '.join(self.languages_frontend)}"


# backend_dev = Backend(experience=5, languages_backend=["Python", "Java"])
# frontend_dev = Frontend(experience=3, languages_frontend=["JavaScript", "HTML", "CSS"])
# fullstack_dev = FullStack(experience=6, languages_backend=["Python", "Java"], languages_frontend=["JavaScript", "HTML", "CSS"])


# backend_dev.coding(10)
# frontend_dev.coding(8)
# fullstack_dev.coding(12)

# print(backend_dev.get_info())
# print(f"Total code time for Backend Developer: {backend_dev.count_code_time} hours")

# print(frontend_dev.get_info())
# print(f"Total code time for Frontend Developer: {frontend_dev.count_code_time} hours")

# print(fullstack_dev.get_info())
# print(f"Total code time for FullStack Developer: {fullstack_dev.count_code_time} hours")



#---------------------
import random

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.account_id = random.randrange(100000, 199999)
        self.transactions_history = {}

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Недостаточно средств для снятия"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            return "Неверная сумма для пополнения"

    def receive(self, amount, sender_account_id):
        if amount > 0:
            if sender_account_id in self.transactions_history:
                self.transactions_history[sender_account_id].append(amount)
            else:
                self.transactions_history[sender_account_id] = [amount]
            self.balance += amount

    def transfer(self, amount, receiving_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            receiving_account.receive(amount, self.account_id)
            return self.balance
        else:
            return "Недостаточно средств для перевода"

# Пример использования класса:
account1 = BankAccount()
account2 = BankAccount()

print("Баланс account1 после создания:", account1.balance)
print("Баланс account2 после создания:", account2.balance)

account1.deposit(7000)
account2.deposit(3000)

print("Баланс account1 после пополнения:", account1.balance)
print("Баланс account2 после пополнения:", account2.balance)

account1.transfer(200, account2)

print("Баланс account1 после перевода:", account1.balance)
print("Баланс account2 после перевода:", account2.balance)

print("История транзакций account1:", account1.transactions_history)
print("История транзакций account2:", account2.transactions_history)
