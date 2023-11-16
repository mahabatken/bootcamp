# "String-stroki"
# "Hello world!My name is John Snow!"


# ''''''
# I'm Jhon Snow.
# I m King jf North!
# ''''''
# print(str1)
# строки-набор последовательных символов,которые мы имспользуем для хранения и представления текстовой информации
# Индексация в строке 
# name="John"
#     #J-0=-4
#     #o-1=-3
#     #h-2=-2
#     #n-3=-1
# print(name)
# print(name[-1])
# str1='word'
# print(str1[0] ,str1 [3])
#Срезы по индексам
# [start:end]
# str1="birthday"
# print(str1)
# print(str1[0:5])
# print(str1[5:7])
# print(str1[:5])
# text="Hello worl!My name is John Snow! I\'m King of North!"
# print(text[::2])
# print(text[::-1])
# конкентинация строк(соединения)+
# a='Hello'
# b='World'
# c=' '
# res = a + b + c
# print(res)

# *
# a ="abc"
# print (a * 5)
#экванирования 
#\n ->перенос строки 
#\t ->горизонтальная табуляция 
# str ='Hello World!\n\tHtllo John!'
# print(str1)

# Форматирования строк 
#  1.с помощью %
#  2.с помощью .format()
#  3.интерполяция(пребывания в срок)f-строки

# name = input('Vvedite imya: ')
# last_name = input('Vvedite familiyu:')
# str1= 'Hello '

# format
# name = input('Vvedite imya: ')
# last_name = input('')
# last_name = input('Vvedite familiyu; ')
# club = "Kipish"
# print('Welcom to the club{},mr/mrs{ {} {}!' . format(club ,name , last_name))
  
# # f-строки
# name = input(''Vvedite imya:')
# last_name = input('Vvedite familiyu; ')
# print(f'Hello mr')


# мeтоды строк -dir 

# print(dri))
# replace(old, new, [count])
# new, заменить count раз если передатиде


# text = "ha ha ha ha"
# res = text.replace("a","e")
# print(text)
# print(f'result after replace: {res}')

# strip()-убираем проблемные символы в начале и в конце строки
# rstrip,lstrip
# a= '  Hello  '
# print(a, len(a))
# res =a.strip()
# print(res, len(res))

# isditit  -
# isnumeris
# isdesimal-            полностью из числа

# a= "56"
# print(a.isdigit())
 
# print("a.Vvedeno chislo:")
# print(f"Vvedeno chislo?:{num.isdigit()}")

# isalpha -состоит ли наша строка из символов алфавита 
# txt = "Hello world"
# print(txt)
# print(txt.isalpha())
# print(res)
# print(res.isalpha())


# text = "Hello John Snow"
# print(text.find("a"))
# print(text.index("a"))


# cont(value, [start])- считает кол-во символов valie внутри строки

# text ="hello 0000 00 0 hello"
# print(text.count("a"))
# print(text.count("o"))
# print ( text.count('hello')
# print ( text.count('hills')     
      

# text = "Let me speak by my heart"
# res = text.split('e')
# print(text)
# print(res)
# print(text.split())

# a = "#hello#hello#hello#hello"
# print(a.split("#"))

# "connector".join(list)-соединяет по connektor строки которые были в list
# ls=a[1:].split("#")
# print(a)
# print(ls) #['hello','life','love','bishkek',]
# print('-'.join(ls))
# swapcase() - переводит все символы в противоположный регистр
# upper() - переводит все в верхний регистр
# lower() - переводит все в нижний регистр

# text = 'Hello WorLD, JOHN snow'
# print(f'Original: {text}')
# print(text.upper())
# print(text.lower())
# print(text.swapcase())

# capitalize() - переводит самый первый символ в верхний регистр
# title() - переводит первые символы всех слов в верхний регистр

          # john.capitalize() -> John
# name = input('Vvedite imya: ').capitalize()
# print(name)
# print(f'Hello! Mr/Mrs {name}!')

# fio = 'jOHN edart snow'
# print(fio.title())
# print(fio.capitalize())
# swapcase() - переводит все символы в противоположный регистр
# upper() - переводит все в верхний регистр
# lower() - переводит все в нижний регистр

# text = 'Hello WorLD, JOHN snow'
# print(f'Original: {text}')
# print(text.upper())
# print(text.lower())
# print(text.swapcase())

# capitalize() - переводит самый первый символ в верхний регистр
# title() - переводит первые символы всех слов в верхний регистр

          # john.capitalize() -> John
# name = input('Vvedite imya: ').capitalize()
# print(name)
# print(f'Hello! Mr/Mrs {name}!')

# fio = 'jOHN edart snow'
# print(fio.title())
# print(fio.capitalize())


#1 
# str1 =  "new "
# print(str1)
#2
# name = "Maha"
# print(name)
# print= (-1)
#3
# name="mysei"
# name = name[::-1]
# print(name[0:2])
#4
# text = "I'm Kyrgyz "
# print(text[: :-1])
#5
# name = input ('Vvedite  login :')
# last_name = input('Vvedite parol: ')
# print(f'Hello mr/mrs{name}{last_name}!Vi yspeshno zapegistpipovan!')
#6
# a="nome"
# print( a * 4)
#7
# name = 'Welcome'
# print(len(name))
#8
# text="The quick brown fox jumps over the lazy dog"
# res = text.replace("o","*")
# print(text)
# print(f'result after replace: {res}')
#9
# text = 'vsem privet'
# print(text.upper())
#10
# text = 'kak dela'
# print(text.lower())
#11
# name = "Bishkek"
# name = list(name)
# print(name)
# name[0], name[-1] = name[-1],name[0]
# print(name)
# print(''.join(name))

#12
# a=" codify#bootcamp#программирование#it#курсы "
# print(a.split("#"))
#13
# name = input('Vvedite imya: ')
# last_name = input('Vvedite familiyu:')
# age = input('vvedite vozrast')
# citi =input('vvedite gorod')
# print(f"ms/mrs your name{name} {last_nam} you age{age} yju live in{citi}")
#14
# name = 'Makers bootcamp'
# print(name[1::2])
#15
# name="abracadabra"
# name[5] = 'K'
# input="".join(name)


















