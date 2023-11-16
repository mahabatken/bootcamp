# Типы данных-Числа-> int,float

#=->оператор присваивания
#varible 
#num =5 
#print(переменная)
#print

#abc-нижний регистр 
#ABC-верхний регист

# #PEPB-правила написания на питоне
# tomorrow_day='27.09.2023'#snake case
# tomorrow_day='27.09.2023'#Camel case

# #+
# num1=5
# num2=15
# print('Result',num1,'+', num2,'=', num1+num2)
#     #Result 5+15=20 

# #-
#primt(55-54)
#print(45-5.5)

#*
# num1=input('Enter the nym1')#->int('5')->5
# num2=input('Enter the nym2')

# num1=int(num1)
# num2=int(num2)

# result=num1*num2
# print(num1,'*', num2,'=',result)


#/and//ant%
#/-обычное деления
#//-деление без остатка
#%-модульное деление(получение остатка от деления)

# num1=10
# num2=4
# print('/',num1/num2)#2.3333333..
# print('//',num1//num2)#2
# print('%',num1%num2)#1

# **
#print(5**2)#5*5
#print(5**3)#5*5*5

#print(9**0.5)#3#квадратный корень

#pow-
#pow(num1,num2,<mod>)
# print(pow(5,3,10))
# print(5**3 % 10)


# #round()-округления числа с плаваюшей точкой
# num1=5.367
# print(round(num1,2))

# abc()-абсолютное значениу числа->  |-67|->67
# a=abs(-16)
# b=abs(16)
# print(a,b)

#divmod(a,b)->Она выводит два числа,первое число это a//b,a вторичное число a % b

# print(divmod(5,2))#2,1
# print(5//2,5 % 2)#2,1

# множественное присваивания
# = это оператор присваивания  
# num1,num2,num3=4,10,7
# print(num1,num2,num3)

# num1,num2=divmod(27,8)
# print(num1,num2)

# import math

# res=math.sqrt(144)
# print(res)#12

# res=math.factorial(235)#2*3*4*5
# print(res)

# r=int(input('введите радиус'))
# число_pi=math.pi

# res_P=2*r*число_pi
# res_S=число_pi*(r**2)
# print('S окружность:',round(res_S,2))
# print('P окружность:',round(res_P,2))   


#1
# numer=int(12)
# print(numer)
#2
# test='new'
# print(test)
#3
# num=7
# strin='new tv'
# print(num*strin)
#4
# num1=8
# num2=6
# print(num1+num2)
#5
# num1=10
# num2=2
# print(num1/num2)
#6
# a = -18
# b =  18
# print( abs(a),abs (b))
# #7
# a=2
# print(pow(6,2))
#8
# a=9
# b=2
# print(a % b)
#9
# a=26
# print(a ** 2 % 5)
#10
# a = int(input('vvedite chislo: ')) 
# b = int(input('vvedite chislo:')) 
# s = int(input('vvedite chislo:')) 
# res = a * b 
# print(res % s )
#11
# a = int(input('vvedite chislo: ')) 
# b = int(input('vvedite chislo:')) 
# s =0.4
# print((a % b) *s )
#12
# num = 24
# print(num ** 2,num ** 3,num ** 0.5)
#13
# k1 = 2
# k2 = 4
# print (math.sqrt(k1 ** 2 + k2** 2))
#14
# r = 11
# print(match.pi * (r **2), 2) )
#15
# x = 3
# y = 5
# z = 7
# x, y, z, = y, z, x
# print(x, y, z)


        день = int(input("Введите количество дней: "))
        время = int(input("Введите количество часов: "))
        минута = int(input("Введите количество минут: "))
        секунда = int(input("Введите количество секунд: "))
        
        total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds
        
        return total_seconds
    except ValueError:
        print("Ошибка: Введите числа!")

total_seconds = get_total_seconds()

if total_seconds is not None:
    print(f"Общее количество секунд: {total_seconds}")
Скопируйте этот код в файл с расширением .py и запустите его с помощью Python. Программа запросит у вас количество дней, часов, минут и секунд, а затем выведет общее количество секунд.

Пример работы программы:

Copy code
Введите количество дней: 2
Введите количество часов: 3
Введите количество минут: 15
Введите количество секунд: 30
Общее количество секунд: 190530













