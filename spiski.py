# list( )-> massivi изменяемый тип данных предситавляюший из себя коллекйию обьектов

# my_list =[[1,"string"],False,None, [1,2,3,4]]
# print(my_list, type(my_list))
# print(my_list[0])
# print(my_list[-1][2])
# print(my_list[2:4])

# range()-vozvrashael posledovatelnost cheselh
# ls = range(1, 10)
# spisok = list(ls)
# print(spisok, type(spisok))

# tuple_ = ("123",)
# print(tuple_,type(tuple_))
# a=(5, 7, 9)
# num1, num2, num3 = a
# print(num1, num2, num3)
# b = 5, 6, 7, 8, 9
# print(b, type(b))

#-------------------------------------------------------------------------------------
# ls = [1, 2, 3, 4, 5, "string", False]

# i = 0
# while i <= 5:
#     print (i)
#     print(ls[i])
#     i = i +1 # increment

# ls = [1, 2 [123, 23, 21], True,Nome, 3, 4, 5, "stribg" False]
# for x in ls:
#     print(x)

# ls =["Maha", "Aiperi","Akilai","Arstan","Atai","Akai"]  
# print(ls, len(ls))
# blak_list = ["Akai", "Atai"]
             
# for name in ls:
#    if name not in blak_list:
#       print(f"We\"re calling to {name}!")   
#    else:
#       print(f "{name}is blak list!")     

# ls -> 1, 21 -> четные числа - квадрат числа
#             ->   нечетные числа - куб числа

# ls = list(range(1, 21))
# print(ls)
# for num in ls:
#     if num % 2 ==0:
#         print(f"chislo {num}chotnoi---> kvadrat: {num **2}")
#     else:
#         print(f"chislo {num}nechotnoi---> kub: {num **3}")   


#---------------------------------------------------------------------------------------------
# metodi spiskov
 
 
# print(dir([]))

# append(element)-
# ls = [1, 2, 3]
# ls.append(4)
# ls.append(5)
# print(ls)
# ls.append([True, False, True])
# print(ls)
#  extent(object) - rasshipaet spisok elementami iz object
# ls = [1, 2, 3]
# print(ls)
# ls.append("Hello")
# ls.append([4, 5, 6])
# print(ls)

# insert(index,element)-dobavlaet element po indeksu
# ls = ["string", 2, 3, False]
# print(ls)
# ls.insert(2, None)
# print(ls)

# remove(element)-ydalaet element is spiska,esli net takogo to bydet oshibka
# pop([index])-ydalaet i vosvrashaet element po index, esli net index to ydalit posledni element

# ls = [5, 1, 2, 3, 4, 5, 5, 5, 5, 5, ]
# print(ls)
# # ls.remove(4)
# # ls.remove(5)
# # print(ls)
# while 5 in ls:
#     ls.remove(5)

# print (ls)  
 
# ls =[5, 1, 2, 3, 4]
# print(ls)
# deleted =ls.pop(15)
# ls.pop(0)
# print(deleted )


# update
# ls = [1, "h,3, 4, 5"]
# ls[1]=2
# print(ls)
# ls.reverse()
# print(ls)
# ls =ls [::-1]
# print(ls)


# from random import randint

# num = randint(0, 100)
# print

# ls = []
# for x in range(0, 50):
#     num = randint(0, 1000)
#     ls.append(num)

# print(ls)
# ls.sort(reverse=True)
# print("AFTER SORTING")
# print(ls)
  

# ls = ["John", "Tirion", "Osmon", "Aibek", "Aijan"]
# print(ls)
# ls.sort(key=len)
# print()
# print(ls)




#1
# num = list([1, "kg pomidor"])
# print(num)

#2
# list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333, ]
# print(list_.count(333))

#3
# list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333,]
# print(list_.index(86))
# print(list)
# deleted = list_.pop(-2)
# print(deleted)

#4
# list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333,]
# list_.sort()
# print(list_)
# list_.reverse()
# print(list_)

#5 
# num1 = ["hello", 1, [1, 'world']]
# num2 = ["mama", 2,["papa"]]
# num1.append(num2)
# print(num1)
# num1.insert(0, num2)
# print(num1)
# num1.extend(num2)
# print(num1)

#6
# tuple_ = (1,)
# print(tuple_,type(tuple_))

#7
# num1 = tuple()
# print(num1)
#8
# tuple_ = ("a", 1, "Hello", True, ["1,b"])
# list = list(tuple_)
# list.remove("Hello")
# print(list)
#9
# tuple_ = ("b", 1, "Hello", True, ['False', "b"])

# print(tuple_[::2])


  



# 1 home w
# a = [1, 1, 2.3, 3 -5, 8, -13, -21, 34.5, 55, 89]
# b = [1, 2.3, 3, 4, -5, 6, 7, 8, 9, -10, 11, -12, -13, 34.5]

# c= []

# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#             break
# print(c)
 
# negetive_list = [num for num in common_elements if num < 0]
# print('Список отрицательных чисел:', negetive_list)
# negetive_list_abs = [abs(num) for num in negetive_list]
# print('Список отрицательныз чисел и абсолютными значениями:', negetive_list_abs)

# common_elements[0] = common_elements[0] ** 3
# common_elements[-1] = common_elements[-1] ** 3
# print("Общийсписок после возведение элементовв степень:", common_elements)


#2
# banknotes = ['Абдылас Малдыбаев', 'Бубусара Бейшеналиева', 'Касым Тыныстанов', 'Тоголок Молдо', 'Курманджан Датка', 'Бенджамин Франклин']
# banknotes[5] = 'Токтогул Сатылганов'
# banknotes.extend(['Алыкул Осмонов', 'Саякбай Каралаев', 'Жусуп Баласагын'])
# denomination_to_index = {1: 0, 5: 1, 10: 2, 20: 3, 50: 4, 100: 5, 200: 6, 500: 7, 1000: 8}
# nominal = int(input("Введите номинал банкноты: "))
# if nominal in denomination_to_index:
#     print(banknotes[denomination_to_index[nominal]])
# else:
#     print("Банкноты с введенным номиналом не существует.")


# 3
# вывод дня недели
# print('Сегодня', weekday + '.')
# проверка пятницы и времени
# if day == 5 and hours < 6:
#     remaining_hours = 6 - hours
#     print('Осталось работать', remaining_hours, 'часа')
#     if remaining_hours < 2:
#         print('Можно уйти пораньше!')
# elif hours < 8:
#     remaining_hours = 8 - hours
#     print('Осталось работать', remaining_hours, 'часа')

#4
# number = int(input('Введите число: ')) 
# if number <= 9 and number >= -9: 
#     print('Число однозначное') 
# else: 
#     print('Двухзначное')

#5
# rating = int(input('Что получил по математике? '))
# if rating == 2:
#  print('Плохо. Марш учиться!')
# if rating == 3:
#  print('Плохо. Марш учиться!')
# if rating == 4:
#  print('Молодец! Можешь отдохнуть.')
# if rating == 5:
#  print('Молодец! Можешь отдохнуть.')

#6
# my_list = [1, '2', 3, 4, '5', 'шесть', 'семь']
# converted_list = [int(x) if str(x).isdigit() else len(str(x)) for x in my_list]
# total_sum = sum(converted_list)
# print(f'Сумма всех элементов списка: {total_sum}')
# even_numbers = [x for x in converted_list if x % 2 == 0]
# odd_numbers = [x for x in converted_list if x % 2 != 0]
# print(f'Список четных чисел: {even_numbers}')
# print(f'Список нечетных чисел: {odd_numbers}')
zadania #4