#Ассоциация означает что внутри обьекта будет существовать другой обьект в качестве атрибутта
# Композиция сильная связь
# Агрегация слабаю связь

# Комрозизия это когда стена не существует отдельно от комнаты Щна создается при 
#создании комнаты и полностью управляется классом комнаты
# Агрегация это когла экцимпляр двигателя создается гдето в другом месте
#  и передается в класс Авто в качесиве параметра

# class Battery:
#     _power = 100

#     def charge(self):
#         if self._power < 100:
#             self._power = 100

#     @property
#     def power(self):
#         return self._power
#     @power.setter
#     def power(self, value):
#         self._power = value


# class Iphone:
#     def __init__(self, color) -> None:
#         self.color = color
#         self.battery = Battery()
#         # когда мы создаем внуири класса обьект от другого класса коипозиция
# a = Iphone("silver")  
# a.battery.power = 50
# print(a.battery.power)
# a.battery.charge()
# print(a.battery.power)
# del a
# # при удалении айфон вместе с ним удаляется батарейка
# class Nokia:
#     def __init__(self, color, battery) -> None:
#         self.color = color
#         self.battery = battery
#         #когда обьект создается из вне класса и передается внутрь агрегации
# battery = Battery()
# nokia1 = Nokia("blak", battery)
# nokia1.battery.power = 50
# print(nokia1.battery.power)
# nokia1.battery.charge()
# print(nokia1.battery.power)
# del nokia1
# nokia2 = Nokia("white", battery)
# print(nokia2.battery.power)
# nokia2.battery.charge()
# print(nokia2.battery.power)  


# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня 
#заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют
# 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.
# from datetime import datetime, timedelta
# from time import sleep
# class Phone:
#     def __init__(self, imei, os):
#         self.__imei = imei
#         self.__os = os
#         self.__battery = 100



#     @property
#     def battery(self):
#         if self.__battery < 0.5:
#             raise Exception("Телефон разряжен!")
#         print(f"Уровень заряда: {self.__battery}")
#         self.__battery -= 0.5    


#     @property
#     def get_info(self):
#         if self.__battery < 0.5:
#             raise Exception("Телефон разряжен!")
#         print(f"OS: {self.__os}, IMEI: {self.__imei}!")
#         self.__battery -= 0.5  


#     def play_mysic(self):
#         if self.__battery < 5:
#             raise Exception("Телефон разряжен!") 
#         print("Слушаем Мирбека А!")
#         self.__battery -= 5  


#     def play_video(self):
#         if self.__battery < 5:
#             raise Exception("Недопустимвй уровень заряда!") 
#         print("Смотрим любимые  клипы!")
#         self.__battery -= 5 



#     def charge_battery(self, sec):
#         now = datetime.now # 11:57:20
#         end = (now() + timedelta(seconds=sec)).strftime("%H:%M:%S")
#         while now().strftime("%H:%M:%S") != end:
#             # print(now().strftime("%H:%M:%S"))
#             sleep(1)
#             if self.__battery < 100:
#                 self.__battery += 1
#                 if self.__battery > 100:
#                     self.__battery = 100
#             print(f"Идет зарядка батареии! Ваш уровень батареи: {self.__battery}!")


# phone = Phone("777", "IQS 16")
# phone.battery
# phone.battery
# phone.get_info
# phone.battery   
# phone.play_mysic()  
# # phone.play_mysic()
# # phone.play_mysic()
# # phone.play_mysic()
# # phone.play_mysic()
# # phone.play_video() 
# # phone.play_video() 
# # phone.play_video() 
# # phone.play_video() 
# # phone.play_video() 
# phone.battery  
# phone.cha



#1 
    
# class Weight:
#     def __init__(self,gramm=0, kilogram=0, centner=0) -> None:
#         self.gramm = gramm
#         self.kilogram = kilogram
#         self.centner = centner

#     def __str__(self):
#         return f"Вес {self.centner} центнеров, {self.kilogram} кг, {self.gramm} гр"




#     def add(self, other):
#         total_grams = (self.centner * 1000000 + self.kilogram * 1000 + self.gramm) + (other.centner * 1000000 + other.kilogram * 1000 + other.gramm)
#         centner, remainder = divmod(total_grams, 1000000)
#         kilogram, gramm = divmod(remainder, 1000)
#         return Weight(centner, kilogram, gramm)

#     def sub(self, other):
#         total_grams = (self.centner * 1000000 + self.kilogram * 1000 + self.gramm) - (other.centner * 1000000 + other.kilogram * 1000 + other.gramm)
#         if total_grams < 0:
#             total_grams = 0
#         centner, remainder = divmod(total_grams, 1000000)
#         kilogram, gramm = divmod(remainder, 1000)
#         return Weight(centner, kilogram, gramm)

#     def __eq__(self, other):
#         return (self.centner, self.kilogram, self.gramm) == (other.centner, other.kilogram, other.gramm)

#     def __lt__(self, other):
#         return (self.centner, self.kilogram, self.gramm) < (other.centner, other.kilogram, other.gramm)

#     def __le__(self, other):
#         return (self.centner, self.kilogram, self.gramm) <= (other.centner, other.kilogram, other.gramm)

#     def __gt__(self, other):
#         return (self.centner, self.kilogram, self.gramm) > (other.centner, other.kilogram, other.gramm)

#     def __ge__(self, other):
#         return (self.centner, self.kilogram, self.gramm) >= (other.centner, other.kilogram, other.gramm)


# if __name__ == '__main__':
#     weight1 = Weight(1, 2, 500)
#     weight2 = Weight(3, 5, 750)

#     print("weight1:", weight1)
#     print("weight2:", weight2)

#     added_weight = weight1.add(weight2)
#     print("Сумма:", added_weight)

#     subtracted_weight = weight2.sub(weight1)
#     print("Разность:", subtracted_weight)

#     print("Сравнение weight1 и weight2:")
#     print("weight1 == weight2:", weight1 == weight2)
#     print("weight1 < weight2:", weight1 < weight2)
#     print("weight1 <= weight2:", weight1 <= weight2)
#     print("weight1 > weight2:", weight1 > weight2)
#     print("weight1 >= weight2:", weight1 >= weight2)
#2
# class Publication:
#     def __init__(self, name, date, pages, library, type):
#         self.name = name
#         self.date = date
#         self.pages = pages
#         self.library = library
#         self.type = type

#     def get_code_in_library(self):
#         library_code = self.library[:2]
#         type_code = self.type[:2]
#         name_code = self.name[:2]
#         date_code = self.date.replace(".", "")
#         return f"{library_code}_{type_code}_{name_code}_{self.pages}_{date_code}"

# class Book(Publication):
#     def __init__(self, name, date, pages, library):
#         super().__init__(name, date, pages, library, type="book")

# class Magazine(Publication):
#     def __init__(self, name, date, pages, library):
#         super().__init__(name, date, pages, library, type="magazine")

# class Newspaper(Publication):
#     def __init__(self, name, date, pages, library):
#         super().__init__(name, date, pages, library, type="newspaper")

# book = Book("Harry Potter", "01.05.2023", 350, "LibA")
# magazine = Magazine("National Geographic", "15.04.2023", 80, "LibB")
# newspaper = Newspaper("New York Times", "30.04.2023", 24, "LibC")

# print(book.get_code_in_library())      
# print(magazine.get_code_in_library())  
# print(newspaper.get_code_in_library())

#3
# class Contact:
#     all_contacts = []

#     def __init__(self,name, lastname,phone_number) -> None:
#         self.name = name
#         self.lastname = lastname
#         self.phone_number = phone_number


# class  Friend(Contact):
#     def play_football_with_me(self):
#         print(f"{self.name} {self.lastname} is playing football with me.")


# class ContactList(list):
#     def search_by_name(self,name):
#         simmilar = [contact for contact in self if name in contact['name']]
#         return simmilar 
# all_contacts = ContactList()


# all_contacts.append({'name': 'Adelina', 'phone': '123-456-7890'})
# all_contacts.append({'name': 'Aielina', 'phone': '987-654-3210'})
# all_contacts.append({'name': 'Hyrel', 'phone': '555845623'})
# all_contacts.append({'name': 'Maha', 'phone': '703177179'})

# name_to_search = 'Hyrel'
# simmilar = all_contacts.search_by_name(name_to_search)

# if simmilar:
#         print(f"Найдены контакты с именем '{name_to_search}':")
#         for contact in simmilar:
#             print(f"Имя: {contact['name']}, Телефон: {contact['phone']}")
# else:
#         print(f"Контакты с именем '{name_to_search}' не найдены.")

